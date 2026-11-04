# Range-Scalp Bot

*Updated Wed Nov 04 19:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47426 | 41299 | 6127 (72) | 6 | $-13658.63 | -4.6% |
| **+10¢** | 35426 | 28317 | 7109 (97) | 7 | $-12497.83 | -5.6% |
| **+15¢** | 29667 | 22012 | 7655 (125) | 8 | $-11466.62 | -6.2% |
| **+20¢** | 26357 | 18340 | 8017 (165) | 9 | $-10119.69 | -6.1% |
| **+10¢ (15¢ stop)** | 57802 | 57709 | 93 (56) | 2 | $-21550.40 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 19:10 | +10 stop | SOL | UP | 0.51 | 0.61 | 0.65 |
| 11-04 19:09 | +10 stop | BNB | UP | 0.59 | open |  |
| 11-04 19:09 | +20 | BNB | UP | 0.59 | open |  |
| 11-04 19:09 | +15 | BNB | UP | 0.59 | open |  |
| 11-04 19:09 | +10 | BNB | UP | 0.59 | open |  |
| 11-04 19:09 | +5 | BNB | UP | 0.59 | open |  |
| 11-04 19:09 | +10 stop | ZEC | UP | 0.71 | 0.55 | -1.93 |
| 11-04 19:08 | +10 stop | BTC | UP | 0.62 | open |  |
| 11-04 19:08 | +20 | BTC | UP | 0.62 | open |  |
| 11-04 19:08 | +15 | BTC | UP | 0.62 | open |  |
| 11-04 19:08 | +10 | BTC | UP | 0.62 | open |  |
| 11-04 19:08 | +5 | BTC | UP | 0.62 | 0.70 | 0.48 |
| 11-04 19:07 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-04 19:07 | +20 | ETH | UP | 0.63 | open |  |
| 11-04 19:07 | +15 | ETH | UP | 0.63 | 0.81 | 1.52 |
| 11-04 19:07 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-04 19:07 | +5 | ETH | UP | 0.63 | 0.68 | 0.17 |
| 11-04 19:07 | +10 stop | SOL | DOWN | 0.67 | 0.48 | -2.24 |
| 11-04 19:07 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-04 19:07 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-04 19:07 | +10 | SOL | DOWN | 0.67 | open |  |
| 11-04 19:07 | +5 | SOL | DOWN | 0.67 | open |  |
| 11-04 19:07 | +10 stop | XRP | DOWN | 0.51 | 0.25 | -2.92 |
| 11-04 19:07 | +20 | XRP | DOWN | 0.51 | open |  |
| 11-04 19:07 | +15 | XRP | DOWN | 0.51 | open |  |
| 11-04 19:07 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-04 19:07 | +5 | XRP | DOWN | 0.52 | open |  |
| 11-04 19:07 | +10 stop | ZEC | DOWN | 0.62 | 0.46 | -1.95 |
| 11-04 19:07 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-04 19:07 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-04 19:07 | +10 | ZEC | DOWN | 0.62 | open |  |
| 11-04 19:07 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-04 19:07 | +10 stop | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-04 19:07 | +20 | DOGE | UP | 0.66 | open |  |
| 11-04 19:07 | +15 | DOGE | UP | 0.66 | open |  |
| 11-04 19:07 | +10 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-04 19:07 | +5 | DOGE | UP | 0.66 | 0.74 | 0.50 |
| 11-04 19:07 | +10 stop | DOGE | DOWN | 0.42 | 0.66 | 2.06 |
| 11-04 19:07 | +20 | DOGE | DOWN | 0.42 | 0.66 | 2.06 |
| 11-04 19:07 | +15 | DOGE | DOWN | 0.43 | 0.66 | 1.96 |
