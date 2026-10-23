# Range-Scalp Bot

*Updated Fri Oct 23 05:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29830 | 25969 | 3861 (39) | 6 | $-8782.28 | -4.7% |
| **+10¢** | 22361 | 17891 | 4470 (55) | 6 | $-7903.90 | -5.6% |
| **+15¢** | 18728 | 13928 | 4800 (78) | 7 | $-7070.88 | -6.0% |
| **+20¢** | 16577 | 11548 | 5029 (101) | 7 | $-6374.63 | -6.1% |
| **+10¢ (15¢ stop)** | 36623 | 36564 | 59 (32) | 3 | $-13810.00 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 05:55 | +10 stop | SOL | UP | 0.52 | 0.62 | 0.65 |
| 10-23 05:55 | +10 stop | DOGE | UP | 0.62 | open |  |
| 10-23 05:55 | +10 stop | NEAR | UP | 0.43 | open |  |
| 10-23 05:55 | +20 | NEAR | UP | 0.43 | open |  |
| 10-23 05:55 | +15 | NEAR | UP | 0.43 | open |  |
| 10-23 05:55 | +10 | NEAR | UP | 0.43 | open |  |
| 10-23 05:55 | +5 | NEAR | UP | 0.43 | 0.50 | 0.34 |
| 10-23 05:54 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 10-23 05:54 | +10 | XRP | DOWN | 0.69 | open |  |
| 10-23 05:54 | +5 | XRP | DOWN | 0.69 | open |  |
| 10-23 05:54 | +5 | SOL | DOWN | 0.66 | open |  |
| 10-23 05:54 | +10 stop | DOGE | UP | 0.69 | 0.51 | -2.13 |
| 10-23 05:54 | +20 | DOGE | UP | 0.69 | open |  |
| 10-23 05:54 | +15 | DOGE | UP | 0.69 | open |  |
| 10-23 05:54 | +10 | DOGE | UP | 0.69 | open |  |
| 10-23 05:54 | +5 | DOGE | UP | 0.69 | open |  |
| 10-23 05:54 | +10 stop | SOL | DOWN | 0.61 | 0.31 | -3.36 |
| 10-23 05:53 | +5 | HYPE | DOWN | 0.71 | open |  |
| 10-23 05:52 | +5 | BNB | UP | 0.67 | 0.80 | 0.99 |
| 10-23 05:52 | +10 stop | ETH | DOWN | 0.57 | 0.70 | 0.97 |
| 10-23 05:52 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 05:52 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 10-23 05:52 | +20 | HYPE | DOWN | 0.60 | open |  |
| 10-23 05:52 | +15 | HYPE | DOWN | 0.60 | open |  |
| 10-23 05:52 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.74 |
| 10-23 05:52 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.33 |
| 10-23 05:51 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 10-23 05:50 | +10 stop | ETH | UP | 0.66 | 0.46 | -2.34 |
| 10-23 05:50 | +5 | ZEC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-23 05:50 | +10 stop | XRP | DOWN | 0.57 | 0.41 | -1.95 |
| 10-23 05:50 | +10 stop | SOL | UP | 0.64 | 0.44 | -2.35 |
| 10-23 05:50 | +10 stop | NEAR | DOWN | 0.69 | 0.82 | 1.05 |
| 10-23 05:49 | +10 stop | ETH | UP | 0.47 | 0.58 | 0.74 |
| 10-23 05:49 | +10 stop | BNB | UP | 0.63 | 0.80 | 1.41 |
| 10-23 05:49 | +20 | BNB | UP | 0.63 | 0.87 | 2.15 |
| 10-23 05:49 | +15 | BNB | UP | 0.63 | 0.80 | 1.41 |
| 10-23 05:49 | +10 | BNB | UP | 0.63 | 0.80 | 1.41 |
| 10-23 05:49 | +5 | BNB | UP | 0.63 | 0.68 | 0.17 |
| 10-23 05:48 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-23 05:48 | +10 stop | ETH | DOWN | 0.51 | 0.36 | -1.85 |
