# Range-Scalp Bot

*Updated Sun Oct 11 09:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11711 | 10096 | 1615 (24) | 4 | $-3973.69 | -5.4% |
| **+10¢** | 8874 | 7000 | 1874 (37) | 4 | $-3767.95 | -6.7% |
| **+15¢** | 7471 | 5485 | 1986 (53) | 4 | $-3230.65 | -6.9% |
| **+20¢** | 6653 | 4588 | 2065 (67) | 7 | $-2708.45 | -6.5% |
| **+10¢ (15¢ stop)** | 14413 | 14372 | 41 (25) | 0 | $-5712.88 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 09:21 | +5 | HYPE | DOWN | 0.66 | open |  |
| 10-11 09:20 | +10 stop | BTC | DOWN | 0.71 | 0.49 | -2.53 |
| 10-11 09:20 | +10 | BTC | DOWN | 0.71 | open |  |
| 10-11 09:20 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-11 09:19 | +10 stop | ZEC | UP | 0.69 | 0.85 | 1.36 |
| 10-11 09:19 | +5 | NEAR | DOWN | 0.67 | open |  |
| 10-11 09:17 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.76 |
| 10-11 09:17 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-11 09:17 | +15 | BNB | DOWN | 0.70 | open |  |
| 10-11 09:17 | +10 | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 10-11 09:17 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 10-11 09:17 | +10 stop | ZEC | DOWN | 0.62 | 0.47 | -1.85 |
| 10-11 09:17 | +20 | ZEC | DOWN | 0.62 | open |  |
| 10-11 09:17 | +15 | ZEC | DOWN | 0.62 | open |  |
| 10-11 09:17 | +10 | ZEC | DOWN | 0.62 | open |  |
| 10-11 09:17 | +5 | ZEC | DOWN | 0.60 | open |  |
| 10-11 09:17 | +10 stop | HYPE | DOWN | 0.69 | 0.51 | -2.13 |
| 10-11 09:17 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-11 09:17 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-11 09:17 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-11 09:17 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-11 09:16 | +10 stop | NEAR | DOWN | 0.70 | 0.48 | -2.53 |
| 10-11 09:16 | +20 | NEAR | DOWN | 0.70 | open |  |
| 10-11 09:16 | +15 | NEAR | DOWN | 0.70 | open |  |
| 10-11 09:16 | +10 | NEAR | DOWN | 0.70 | open |  |
| 10-11 09:16 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-11 09:16 | +5 | SOL | DOWN | 0.64 | 0.70 | 0.28 |
| 10-11 09:16 | +10 stop | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-11 09:16 | +20 | BTC | DOWN | 0.55 | open |  |
| 10-11 09:16 | +15 | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 10-11 09:16 | +10 | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-11 09:16 | +5 | BTC | DOWN | 0.55 | 0.65 | 0.66 |
| 10-11 09:16 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-11 09:16 | +20 | SOL | DOWN | 0.63 | 0.83 | 1.73 |
| 10-11 09:16 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-11 09:16 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 10-11 09:16 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.17 |
| 10-11 09:16 | +10 stop | DOGE | DOWN | 0.69 | 0.79 | 0.73 |
| 10-11 09:16 | +20 | DOGE | DOWN | 0.69 | open |  |
| 10-11 09:16 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
