# Range-Scalp Bot

*Updated Thu Oct 08 19:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7931 | 6875 | 1056 (13) | 0 | $-2466.02 | -4.9% |
| **+10¢** | 6006 | 4752 | 1254 (24) | 1 | $-2458.89 | -6.5% |
| **+15¢** | 5048 | 3733 | 1315 (32) | 5 | $-1991.93 | -6.3% |
| **+20¢** | 4508 | 3145 | 1363 (40) | 5 | $-1562.12 | -5.5% |
| **+10¢ (15¢ stop)** | 9628 | 9599 | 29 (18) | 1 | $-3538.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 19:33 | +5 | ETH | UP | 0.67 | 0.73 | 0.30 |
| 10-08 19:33 | +10 stop | ETH | UP | 0.61 | 0.73 | 0.89 |
| 10-08 19:33 | +20 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-08 19:33 | +15 | ETH | UP | 0.61 | 0.81 | 1.72 |
| 10-08 19:33 | +10 | ETH | UP | 0.61 | 0.73 | 0.89 |
| 10-08 19:33 | +5 | ETH | UP | 0.60 | 0.66 | 0.27 |
| 10-08 19:32 | +5 | BNB | UP | 0.71 | 0.77 | 0.32 |
| 10-08 19:31 | +10 stop | HYPE | UP | 0.57 | 0.69 | 0.87 |
| 10-08 19:31 | +20 | HYPE | UP | 0.59 | open |  |
| 10-08 19:31 | +15 | HYPE | UP | 0.61 | open |  |
| 10-08 19:31 | +10 | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 10-08 19:31 | +5 | HYPE | UP | 0.61 | 0.69 | 0.48 |
| 10-08 19:31 | +10 stop | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-08 19:31 | +20 | BTC | UP | 0.69 | open |  |
| 10-08 19:31 | +15 | BTC | UP | 0.69 | open |  |
| 10-08 19:31 | +10 | BTC | UP | 0.69 | 0.79 | 0.73 |
| 10-08 19:31 | +5 | BTC | UP | 0.68 | 0.79 | 0.82 |
| 10-08 19:31 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-08 19:31 | +20 | NEAR | UP | 0.69 | open |  |
| 10-08 19:31 | +15 | NEAR | UP | 0.69 | open |  |
| 10-08 19:31 | +10 | NEAR | UP | 0.69 | open |  |
| 10-08 19:31 | +5 | NEAR | UP | 0.69 | 0.77 | 0.48 |
| 10-08 19:31 | +10 stop | DOGE | UP | 0.64 | 0.76 | 0.90 |
| 10-08 19:31 | +20 | DOGE | UP | 0.64 | open |  |
| 10-08 19:31 | +15 | DOGE | UP | 0.64 | open |  |
| 10-08 19:31 | +10 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 10-08 19:31 | +5 | DOGE | UP | 0.65 | 0.76 | 0.82 |
| 10-08 19:31 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.83 |
| 10-08 19:31 | +20 | BNB | UP | 0.64 | open |  |
| 10-08 19:31 | +15 | BNB | UP | 0.64 | open |  |
| 10-08 19:31 | +10 | BNB | UP | 0.62 | 0.77 | 1.20 |
| 10-08 19:31 | +5 | BNB | UP | 0.62 | 0.67 | 0.17 |
| 10-08 19:31 | +10 stop | SOL | UP | 0.63 | 0.75 | 0.89 |
| 10-08 19:31 | +20 | SOL | UP | 0.63 | 0.84 | 1.83 |
| 10-08 19:31 | +15 | SOL | UP | 0.63 | 0.84 | 1.83 |
| 10-08 19:31 | +10 | SOL | UP | 0.62 | 0.75 | 0.94 |
| 10-08 19:31 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 10-08 19:22 | +10 stop | HYPE | DOWN | 0.25 | 0.61 | 3.29 |
| 10-08 19:21 | +5 | HYPE | DOWN | 0.61 | yes | -6.27 |
| 10-08 19:21 | +10 stop | ZEC | UP | 0.59 | 0.72 | 0.97 |
