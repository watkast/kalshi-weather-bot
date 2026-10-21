# Range-Scalp Bot

*Updated Wed Oct 21 10:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 27049 | 23551 | 3498 (39) | 4 | $-7882.61 | -4.6% |
| **+10¢** | 20351 | 16310 | 4041 (55) | 4 | $-6965.71 | -5.4% |
| **+15¢** | 17036 | 12686 | 4350 (78) | 6 | $-6247.15 | -5.8% |
| **+20¢** | 15084 | 10526 | 4558 (97) | 6 | $-5603.47 | -5.9% |
| **+10¢ (15¢ stop)** | 33186 | 33127 | 59 (32) | 2 | $-12274.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-21 10:22 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 10-21 10:22 | +15 | XRP | DOWN | 0.67 | open |  |
| 10-21 10:22 | +10 | XRP | DOWN | 0.67 | open |  |
| 10-21 10:22 | +5 | XRP | DOWN | 0.67 | open |  |
| 10-21 10:22 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-21 10:22 | +10 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-21 10:22 | +5 | ETH | DOWN | 0.62 | 0.73 | 0.79 |
| 10-21 10:20 | +5 | SOL | DOWN | 0.69 | open |  |
| 10-21 10:20 | +5 | BNB | DOWN | 0.69 | open |  |
| 10-21 10:20 | +5 | BNB | DOWN | 0.60 | 0.69 | 0.58 |
| 10-21 10:19 | +10 stop | ZEC | DOWN | 0.47 | 0.32 | -1.84 |
| 10-21 10:19 | +5 | BNB | DOWN | 0.60 | 0.67 | 0.37 |
| 10-21 10:19 | +10 stop | SOL | DOWN | 0.64 | 0.47 | -2.05 |
| 10-21 10:19 | +20 | SOL | DOWN | 0.64 | open |  |
| 10-21 10:19 | +15 | SOL | DOWN | 0.64 | open |  |
| 10-21 10:19 | +10 | SOL | DOWN | 0.64 | open |  |
| 10-21 10:19 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.48 |
| 10-21 10:19 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-21 10:19 | +20 | BTC | DOWN | 0.67 | open |  |
| 10-21 10:19 | +15 | BTC | DOWN | 0.67 | open |  |
| 10-21 10:19 | +10 | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-21 10:19 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-21 10:17 | +5 | ZEC | DOWN | 0.67 | open |  |
| 10-21 10:17 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-21 10:17 | +20 | BNB | DOWN | 0.64 | open |  |
| 10-21 10:17 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-21 10:17 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-21 10:17 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.23 |
| 10-21 10:17 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.70 |
| 10-21 10:17 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-21 10:17 | +15 | XRP | DOWN | 0.63 | 0.81 | 1.52 |
| 10-21 10:17 | +10 | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 10-21 10:17 | +5 | XRP | DOWN | 0.63 | 0.69 | 0.28 |
| 10-21 10:16 | +10 stop | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 10-21 10:16 | +20 | HYPE | DOWN | 0.68 | 0.91 | 2.02 |
| 10-21 10:16 | +15 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 10-21 10:16 | +10 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 10-21 10:16 | +5 | HYPE | DOWN | 0.67 | 0.84 | 1.44 |
| 10-21 10:15 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-21 10:15 | +20 | ETH | DOWN | 0.67 | open |  |
