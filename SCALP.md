# Range-Scalp Bot

*Updated Fri Nov 06 22:47 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50078 | 43653 | 6425 (76) | 1 | $-14066.85 | -4.5% |
| **+10¢** | 37376 | 29899 | 7477 (102) | 2 | $-12972.62 | -5.5% |
| **+15¢** | 31303 | 23244 | 8059 (131) | 2 | $-11895.93 | -6.1% |
| **+20¢** | 27831 | 19381 | 8450 (173) | 2 | $-10518.06 | -6.0% |
| **+10¢ (15¢ stop)** | 60997 | 60898 | 99 (58) | 2 | $-22617.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 22:46 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-06 22:46 | +20 | HYPE | DOWN | 0.70 | open |  |
| 11-06 22:46 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-06 22:46 | +10 | HYPE | DOWN | 0.70 | open |  |
| 11-06 22:46 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-06 22:46 | +10 stop | XRP | DOWN | 0.68 | open |  |
| 11-06 22:46 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-06 22:46 | +15 | XRP | DOWN | 0.68 | open |  |
| 11-06 22:46 | +10 | XRP | DOWN | 0.67 | open |  |
| 11-06 22:46 | +5 | XRP | DOWN | 0.67 | 0.72 | 0.19 |
| 11-06 22:42 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-06 22:40 | +10 stop | BTC | DOWN | 0.60 | 0.29 | -3.42 |
| 11-06 22:40 | +20 | BTC | DOWN | 0.60 | yes | -6.17 |
| 11-06 22:40 | +10 | BTC | DOWN | 0.60 | yes | -6.17 |
| 11-06 22:40 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 11-06 22:40 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-06 22:38 | +10 stop | SOL | DOWN | 0.64 | 0.48 | -1.95 |
| 11-06 22:38 | +5 | ETH | UP | 0.61 | 0.67 | 0.27 |
| 11-06 22:36 | +10 stop | SOL | DOWN | 0.67 | 0.46 | -2.44 |
| 11-06 22:36 | +10 stop | BNB | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 22:36 | +10 stop | DOGE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-06 22:35 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-06 22:35 | +15 | BTC | DOWN | 0.71 | yes | -7.25 |
| 11-06 22:35 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-06 22:35 | +5 | BTC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-06 22:35 | +5 | ETH | UP | 0.54 | 0.61 | 0.35 |
| 11-06 22:35 | +10 stop | BNB | DOWN | 0.64 | 0.45 | -2.25 |
| 11-06 22:35 | +10 stop | DOGE | DOWN | 0.66 | 0.45 | -2.44 |
| 11-06 22:34 | +10 stop | HYPE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-06 22:34 | +5 | SOL | UP | 0.54 | no | -5.58 |
| 11-06 22:33 | +10 stop | HYPE | DOWN | 0.65 | 0.46 | -2.24 |
| 11-06 22:33 | +10 | HYPE | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 22:32 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 22:32 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-06 22:32 | +15 | NEAR | DOWN | 0.65 | 0.82 | 1.43 |
| 11-06 22:32 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-06 22:32 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-06 22:32 | +10 stop | BTC | DOWN | 0.57 | 0.71 | 1.07 |
| 11-06 22:32 | +20 | BTC | DOWN | 0.57 | 0.78 | 1.79 |
| 11-06 22:32 | +15 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
