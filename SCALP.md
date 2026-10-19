# Range-Scalp Bot

*Updated Mon Oct 19 23:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 24746 | 21545 | 3201 (31) | 6 | $-7220.35 | -4.6% |
| **+10¢** | 18608 | 14909 | 3699 (46) | 7 | $-6429.20 | -5.5% |
| **+15¢** | 15573 | 11590 | 3983 (70) | 9 | $-5791.64 | -5.9% |
| **+20¢** | 13767 | 9596 | 4171 (88) | 9 | $-5213.23 | -6.0% |
| **+10¢ (15¢ stop)** | 30394 | 30342 | 52 (30) | 0 | $-11401.44 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 23:24 | +10 stop | BTC | DOWN | 0.61 | 0.31 | -3.32 |
| 10-19 23:24 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-19 23:24 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-19 23:24 | +5 | BTC | DOWN | 0.61 | open |  |
| 10-19 23:23 | +10 stop | BNB | UP | 0.59 | 0.73 | 1.06 |
| 10-19 23:23 | +10 stop | XRP | UP | 0.67 | 0.82 | 1.23 |
| 10-19 23:23 | +10 stop | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-19 23:23 | +10 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-19 23:23 | +5 | ETH | UP | 0.57 | 0.77 | 1.69 |
| 10-19 23:23 | +10 stop | SOL | UP | 0.62 | 0.84 | 1.93 |
| 10-19 23:23 | +10 | SOL | UP | 0.64 | 0.84 | 1.73 |
| 10-19 23:23 | +5 | SOL | UP | 0.64 | 0.71 | 0.38 |
| 10-19 23:22 | +10 stop | ETH | DOWN | 0.43 | 0.55 | 0.84 |
| 10-19 23:22 | +10 | ETH | DOWN | 0.43 | 0.55 | 0.84 |
| 10-19 23:22 | +5 | ETH | DOWN | 0.43 | 0.55 | 0.84 |
| 10-19 23:22 | +10 | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 23:22 | +10 stop | BNB | DOWN | 0.53 | 0.38 | -1.85 |
| 10-19 23:22 | +10 stop | SOL | DOWN | 0.61 | 0.40 | -2.44 |
| 10-19 23:22 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-19 23:22 | +10 stop | HYPE | UP | 0.52 | 0.72 | 1.67 |
| 10-19 23:21 | +10 stop | DOGE | UP | 0.61 | 0.42 | -2.25 |
| 10-19 23:21 | +5 | DOGE | UP | 0.61 | 0.75 | 1.09 |
| 10-19 23:20 | +10 stop | ZEC | UP | 0.69 | 0.81 | 0.94 |
| 10-19 23:20 | +5 | SOL | UP | 0.59 | 0.64 | 0.16 |
| 10-19 23:20 | +10 stop | ZEC | DOWN | 0.40 | 0.54 | 1.05 |
| 10-19 23:20 | +10 stop | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 10-19 23:20 | +10 stop | BNB | DOWN | 0.66 | 0.48 | -2.14 |
| 10-19 23:20 | +20 | BNB | DOWN | 0.66 | open |  |
| 10-19 23:20 | +15 | BNB | DOWN | 0.66 | open |  |
| 10-19 23:20 | +10 | BNB | DOWN | 0.66 | open |  |
| 10-19 23:20 | +5 | BNB | DOWN | 0.66 | open |  |
| 10-19 23:19 | +10 stop | HYPE | UP | 0.66 | 0.81 | 1.19 |
| 10-19 23:19 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 10-19 23:19 | +10 stop | XRP | UP | 0.66 | 0.76 | 0.71 |
| 10-19 23:19 | +10 stop | SOL | DOWN | 0.57 | 0.35 | -2.54 |
| 10-19 23:19 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-19 23:19 | +10 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-19 23:19 | +5 | SOL | DOWN | 0.56 | 0.64 | 0.45 |
| 10-19 23:19 | +10 stop | ETH | DOWN | 0.61 | 0.71 | 0.68 |
| 10-19 23:19 | +15 | ETH | DOWN | 0.61 | open |  |
