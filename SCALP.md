# Range-Scalp Bot

*Updated Fri Oct 30 23:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41396 | 36129 | 5267 (54) | 2 | $-11561.48 | -4.4% |
| **+10¢** | 30855 | 24762 | 6093 (78) | 4 | $-10285.55 | -5.3% |
| **+15¢** | 25791 | 19225 | 6566 (106) | 4 | $-9347.00 | -5.8% |
| **+20¢** | 22891 | 16015 | 6876 (137) | 6 | $-8217.40 | -5.7% |
| **+10¢ (15¢ stop)** | 50456 | 50381 | 75 (41) | 0 | $-19060.27 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 23:03 | +10 stop | XRP | UP | 0.70 | 0.83 | 1.05 |
| 10-30 23:03 | +5 | XRP | UP | 0.70 | 0.75 | 0.21 |
| 10-30 23:03 | +10 stop | DOGE | UP | 0.56 | 0.69 | 0.97 |
| 10-30 23:02 | +5 | BTC | UP | 0.65 | 0.76 | 0.81 |
| 10-30 23:02 | +5 | XRP | UP | 0.54 | 0.62 | 0.45 |
| 10-30 23:02 | +10 stop | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-30 23:02 | +20 | NEAR | UP | 0.71 | 0.91 | 1.82 |
| 10-30 23:02 | +15 | NEAR | UP | 0.71 | 0.87 | 1.37 |
| 10-30 23:02 | +10 | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-30 23:02 | +5 | NEAR | UP | 0.71 | 0.82 | 0.84 |
| 10-30 23:02 | +10 stop | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 10-30 23:02 | +20 | HYPE | UP | 0.65 | open |  |
| 10-30 23:02 | +15 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 10-30 23:02 | +10 | HYPE | UP | 0.65 | 0.77 | 0.91 |
| 10-30 23:02 | +5 | HYPE | UP | 0.65 | 0.73 | 0.50 |
| 10-30 23:02 | +5 | DOGE | DOWN | 0.57 | open |  |
| 10-30 23:02 | +10 stop | ETH | UP | 0.63 | 0.78 | 1.20 |
| 10-30 23:02 | +15 | ETH | UP | 0.63 | 0.78 | 1.20 |
| 10-30 23:02 | +10 | ETH | UP | 0.62 | 0.78 | 1.30 |
| 10-30 23:02 | +5 | ETH | UP | 0.62 | 0.68 | 0.27 |
| 10-30 23:02 | +10 stop | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-30 23:02 | +20 | ZEC | UP | 0.68 | 0.89 | 1.87 |
| 10-30 23:02 | +15 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-30 23:02 | +10 | ZEC | UP | 0.68 | 0.79 | 0.82 |
| 10-30 23:02 | +5 | ZEC | UP | 0.68 | 0.73 | 0.20 |
| 10-30 23:01 | +5 | SOL | DOWN | 0.57 | open |  |
| 10-30 23:01 | +10 stop | BTC | DOWN | 0.54 | 0.35 | -2.24 |
| 10-30 23:01 | +20 | BTC | DOWN | 0.54 | open |  |
| 10-30 23:01 | +15 | BTC | DOWN | 0.54 | open |  |
| 10-30 23:01 | +10 | BTC | DOWN | 0.54 | open |  |
| 10-30 23:01 | +5 | BTC | DOWN | 0.54 | 0.59 | 0.15 |
| 10-30 23:01 | +10 stop | BNB | UP | 0.65 | 0.81 | 1.30 |
| 10-30 23:01 | +20 | BNB | UP | 0.65 | 0.86 | 1.81 |
| 10-30 23:01 | +15 | BNB | UP | 0.65 | 0.81 | 1.30 |
| 10-30 23:01 | +10 | BNB | UP | 0.65 | 0.81 | 1.30 |
| 10-30 23:01 | +5 | BNB | UP | 0.65 | 0.73 | 0.46 |
| 10-30 23:01 | +10 stop | XRP | DOWN | 0.51 | 0.36 | -1.85 |
| 10-30 23:01 | +20 | XRP | DOWN | 0.51 | open |  |
| 10-30 23:01 | +15 | XRP | DOWN | 0.51 | open |  |
| 10-30 23:01 | +10 | XRP | DOWN | 0.51 | open |  |
