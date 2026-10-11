# Range-Scalp Bot

*Updated Sun Oct 11 13:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11964 | 10324 | 1640 (24) | 3 | $-3982.77 | -5.3% |
| **+10¢** | 9078 | 7171 | 1907 (37) | 3 | $-3787.56 | -6.6% |
| **+15¢** | 7647 | 5623 | 2024 (54) | 4 | $-3231.18 | -6.7% |
| **+20¢** | 6815 | 4710 | 2105 (67) | 4 | $-2710.40 | -6.3% |
| **+10¢ (15¢ stop)** | 14730 | 14689 | 41 (25) | 0 | $-5826.99 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 13:13 | +10 stop | NEAR | UP | 0.64 | 0.82 | 1.52 |
| 10-11 13:12 | +10 stop | ETH | DOWN | 0.62 | 0.09 | -5.58 |
| 10-11 13:12 | +20 | ETH | DOWN | 0.62 | open |  |
| 10-11 13:12 | +15 | ETH | DOWN | 0.62 | open |  |
| 10-11 13:12 | +10 | ETH | DOWN | 0.62 | open |  |
| 10-11 13:12 | +5 | ETH | DOWN | 0.63 | open |  |
| 10-11 13:12 | +10 stop | NEAR | UP | 0.54 | 0.73 | 1.58 |
| 10-11 13:12 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-11 13:12 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-11 13:12 | +15 | ZEC | DOWN | 0.69 | open |  |
| 10-11 13:12 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-11 13:12 | +5 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 10-11 13:11 | +10 stop | NEAR | DOWN | 0.58 | 0.31 | -3.03 |
| 10-11 13:11 | +10 | NEAR | DOWN | 0.58 | open |  |
| 10-11 13:11 | +5 | NEAR | DOWN | 0.58 | open |  |
| 10-11 13:10 | +10 stop | NEAR | UP | 0.71 | 0.35 | -3.91 |
| 10-11 13:08 | +10 stop | NEAR | DOWN | 0.66 | 0.42 | -2.74 |
| 10-11 13:06 | +10 stop | NEAR | DOWN | 0.51 | 0.61 | 0.66 |
| 10-11 13:05 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.77 |
| 10-11 13:03 | +10 stop | NEAR | DOWN | 0.67 | 0.47 | -2.34 |
| 10-11 13:03 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-11 13:03 | +20 | BTC | DOWN | 0.71 | 0.93 | 1.96 |
| 10-11 13:03 | +15 | BTC | DOWN | 0.71 | 0.93 | 1.96 |
| 10-11 13:03 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-11 13:03 | +5 | BTC | DOWN | 0.71 | 0.80 | 0.63 |
| 10-11 13:02 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.93 |
| 10-11 13:02 | +10 stop | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 13:02 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-11 13:02 | +15 | ETH | DOWN | 0.66 | 0.83 | 1.44 |
| 10-11 13:02 | +10 | ETH | DOWN | 0.66 | 0.78 | 0.91 |
| 10-11 13:02 | +5 | ETH | DOWN | 0.66 | 0.72 | 0.29 |
| 10-11 13:01 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +15 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +5 | HYPE | DOWN | 0.69 | open |  |
| 10-11 13:01 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 0.99 |
| 10-11 13:01 | +20 | XRP | DOWN | 0.65 | 0.88 | 2.04 |
| 10-11 13:01 | +15 | XRP | DOWN | 0.65 | 0.82 | 1.41 |
| 10-11 13:01 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.92 |
| 10-11 13:01 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.30 |
