# Range-Scalp Bot

*Updated Mon Oct 19 23:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24763 | 21556 | 3207 (31) | 8 | $-7256.43 | -4.7% |
| **+10¢** | 18620 | 14914 | 3706 (46) | 8 | $-6471.12 | -5.5% |
| **+15¢** | 15582 | 11590 | 3992 (70) | 9 | $-5848.25 | -6.0% |
| **+20¢** | 13776 | 9596 | 4180 (88) | 9 | $-5270.25 | -6.1% |
| **+10¢ (15¢ stop)** | 30411 | 30359 | 52 (30) | 2 | $-11413.02 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 23:35 | +10 stop | SOL | UP | 0.70 | 0.47 | -2.63 |
| 10-19 23:35 | +5 | XRP | UP | 0.66 | open |  |
| 10-19 23:35 | +5 | NEAR | UP | 0.60 | open |  |
| 10-19 23:34 | +10 stop | NEAR | DOWN | 0.49 | open |  |
| 10-19 23:34 | +10 | NEAR | DOWN | 0.49 | open |  |
| 10-19 23:34 | +5 | NEAR | DOWN | 0.49 | 0.54 | 0.14 |
| 10-19 23:34 | +10 stop | ETH | UP | 0.66 | 0.76 | 0.71 |
| 10-19 23:34 | +5 | ETH | UP | 0.65 | 0.70 | 0.19 |
| 10-19 23:34 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-19 23:34 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-19 23:34 | +10 stop | SOL | UP | 0.56 | 0.67 | 0.76 |
| 10-19 23:33 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-19 23:33 | +10 stop | BNB | UP | 0.71 | 0.81 | 0.74 |
| 10-19 23:33 | +10 stop | BTC | UP | 0.70 | 0.51 | -2.23 |
| 10-19 23:33 | +20 | BTC | UP | 0.70 | open |  |
| 10-19 23:33 | +15 | BTC | UP | 0.70 | open |  |
| 10-19 23:33 | +10 | BTC | UP | 0.70 | open |  |
| 10-19 23:33 | +5 | BTC | UP | 0.70 | open |  |
| 10-19 23:33 | +10 stop | ZEC | UP | 0.70 | 0.82 | 0.94 |
| 10-19 23:33 | +10 stop | XRP | DOWN | 0.53 | open |  |
| 10-19 23:33 | +10 | XRP | DOWN | 0.53 | open |  |
| 10-19 23:33 | +5 | XRP | DOWN | 0.53 | 0.59 | 0.25 |
| 10-19 23:33 | +10 stop | HYPE | DOWN | 0.52 | 0.27 | -2.82 |
| 10-19 23:33 | +10 | HYPE | DOWN | 0.51 | 0.61 | 0.65 |
| 10-19 23:33 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 10-19 23:32 | +5 | SOL | DOWN | 0.65 | open |  |
| 10-19 23:32 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 10-19 23:32 | +5 | HYPE | DOWN | 0.68 | open |  |
| 10-19 23:32 | +10 stop | BNB | DOWN | 0.53 | 0.38 | -1.85 |
| 10-19 23:32 | +20 | BNB | DOWN | 0.53 | open |  |
| 10-19 23:32 | +15 | BNB | DOWN | 0.53 | open |  |
| 10-19 23:32 | +10 | BNB | DOWN | 0.53 | open |  |
| 10-19 23:32 | +5 | BNB | DOWN | 0.53 | open |  |
| 10-19 23:31 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-19 23:31 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-19 23:31 | +15 | XRP | DOWN | 0.63 | open |  |
| 10-19 23:31 | +10 | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 10-19 23:31 | +5 | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 10-19 23:31 | +10 stop | SOL | DOWN | 0.56 | 0.35 | -2.44 |
| 10-19 23:31 | +20 | SOL | DOWN | 0.56 | open |  |
