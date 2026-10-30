# Range-Scalp Bot

*Updated Fri Oct 30 23:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41422 | 36149 | 5273 (54) | 3 | $-11588.04 | -4.4% |
| **+10¢** | 30876 | 24775 | 6101 (78) | 3 | $-10323.98 | -5.3% |
| **+15¢** | 25810 | 19234 | 6576 (106) | 3 | $-9395.20 | -5.8% |
| **+20¢** | 22912 | 16025 | 6887 (137) | 3 | $-8264.11 | -5.7% |
| **+10¢ (15¢ stop)** | 50486 | 50411 | 75 (41) | 0 | $-19087.23 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 23:33 | +5 | NEAR | UP | 0.63 | open |  |
| 10-30 23:33 | +10 stop | BNB | UP | 0.62 | 0.78 | 1.30 |
| 10-30 23:32 | +5 | HYPE | UP | 0.70 | 0.77 | 0.42 |
| 10-30 23:32 | +10 stop | NEAR | UP | 0.54 | 0.37 | -2.05 |
| 10-30 23:32 | +20 | NEAR | UP | 0.54 | open |  |
| 10-30 23:32 | +15 | NEAR | UP | 0.54 | open |  |
| 10-30 23:32 | +10 | NEAR | UP | 0.54 | open |  |
| 10-30 23:32 | +5 | NEAR | UP | 0.54 | 0.61 | 0.35 |
| 10-30 23:32 | +10 stop | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-30 23:32 | +20 | HYPE | UP | 0.59 | 0.83 | 2.13 |
| 10-30 23:32 | +15 | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-30 23:32 | +10 | HYPE | UP | 0.59 | 0.77 | 1.50 |
| 10-30 23:32 | +5 | HYPE | UP | 0.59 | 0.67 | 0.47 |
| 10-30 23:31 | +10 stop | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 10-30 23:31 | +20 | DOGE | UP | 0.70 | 0.91 | 1.88 |
| 10-30 23:31 | +15 | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 10-30 23:31 | +10 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 10-30 23:31 | +5 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 10-30 23:31 | +10 stop | BTC | DOWN | 0.52 | 0.29 | -2.63 |
| 10-30 23:31 | +20 | BTC | DOWN | 0.52 | open |  |
| 10-30 23:31 | +15 | BTC | DOWN | 0.52 | open |  |
| 10-30 23:31 | +10 | BTC | DOWN | 0.52 | open |  |
| 10-30 23:31 | +5 | BTC | DOWN | 0.52 | open |  |
| 10-30 23:31 | +10 stop | BNB | DOWN | 0.53 | 0.35 | -2.14 |
| 10-30 23:31 | +20 | BNB | DOWN | 0.53 | open |  |
| 10-30 23:31 | +15 | BNB | DOWN | 0.53 | open |  |
| 10-30 23:31 | +10 | BNB | DOWN | 0.53 | open |  |
| 10-30 23:31 | +5 | BNB | DOWN | 0.53 | open |  |
| 10-30 23:31 | +10 stop | XRP | UP | 0.64 | 0.78 | 1.10 |
| 10-30 23:31 | +20 | XRP | UP | 0.65 | 0.91 | 2.37 |
| 10-30 23:31 | +15 | XRP | UP | 0.65 | 0.82 | 1.43 |
| 10-30 23:31 | +10 | XRP | UP | 0.65 | 0.78 | 1.01 |
| 10-30 23:31 | +5 | XRP | UP | 0.64 | 0.78 | 1.10 |
| 10-30 23:31 | +10 stop | SOL | UP | 0.68 | 0.84 | 1.34 |
| 10-30 23:31 | +20 | SOL | UP | 0.68 | 0.88 | 1.76 |
| 10-30 23:31 | +15 | SOL | UP | 0.68 | 0.84 | 1.34 |
| 10-30 23:31 | +10 | SOL | UP | 0.68 | 0.84 | 1.34 |
| 10-30 23:31 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 10-30 23:26 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 10-30 23:26 | +20 | XRP | UP | 0.71 | 0.92 | 1.84 |
