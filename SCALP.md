# Range-Scalp Bot

*Updated Sun Nov 01 19:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43862 | 38210 | 5652 (65) | 3 | $-12570.47 | -4.6% |
| **+10¢** | 32727 | 26196 | 6531 (86) | 3 | $-11319.99 | -5.5% |
| **+15¢** | 27385 | 20355 | 7030 (113) | 5 | $-10341.57 | -6.0% |
| **+20¢** | 24323 | 16960 | 7363 (147) | 5 | $-9127.37 | -6.0% |
| **+10¢ (15¢ stop)** | 53500 | 53414 | 86 (51) | 3 | $-20238.18 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 19:32 | +5 | BTC | DOWN | 0.67 | open |  |
| 11-01 19:32 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-01 19:31 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-01 19:31 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-01 19:31 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-01 19:31 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-01 19:31 | +5 | NEAR | DOWN | 0.69 | open |  |
| 11-01 19:31 | +10 stop | ETH | DOWN | 0.62 | open |  |
| 11-01 19:31 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-01 19:31 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-01 19:31 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-01 19:31 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 11-01 19:31 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 19:31 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-01 19:31 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-01 19:31 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 19:31 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-01 19:31 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 11-01 19:31 | +20 | BTC | DOWN | 0.63 | open |  |
| 11-01 19:31 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-01 19:31 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-01 19:31 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-01 19:31 | +10 stop | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-01 19:31 | +20 | BNB | DOWN | 0.59 | open |  |
| 11-01 19:31 | +15 | BNB | DOWN | 0.59 | open |  |
| 11-01 19:31 | +10 | BNB | DOWN | 0.59 | 0.73 | 1.09 |
| 11-01 19:31 | +5 | BNB | DOWN | 0.59 | 0.67 | 0.47 |
| 11-01 19:22 | +10 stop | HYPE | UP | 0.71 | 0.88 | 1.47 |
| 11-01 19:20 | +10 stop | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-01 19:20 | +10 stop | NEAR | UP | 0.56 | 0.68 | 0.86 |
| 11-01 19:20 | +10 stop | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-01 19:19 | +10 stop | XRP | DOWN | 0.59 | 0.41 | -2.14 |
| 11-01 19:19 | +10 stop | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-01 19:19 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 11-01 19:18 | +10 | ZEC | UP | 0.71 | 0.82 | 0.84 |
| 11-01 19:18 | +5 | ZEC | UP | 0.71 | 0.77 | 0.32 |
| 11-01 19:18 | +10 stop | HYPE | UP | 0.62 | 0.42 | -2.35 |
| 11-01 19:18 | +5 | HYPE | UP | 0.62 | 0.70 | 0.48 |
| 11-01 19:18 | +10 stop | SOL | UP | 0.71 | 0.81 | 0.74 |
| 11-01 19:18 | +20 | SOL | UP | 0.71 | 0.92 | 1.91 |
