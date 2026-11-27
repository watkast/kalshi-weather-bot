# Range-Scalp Bot

*Updated Fri Nov 27 06:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73463 | 64113 | 9350 (165) | 4 | $-19574.19 | -4.2% |
| **+10¢** | 54742 | 43825 | 10917 (210) | 6 | $-18193.05 | -5.3% |
| **+15¢** | 45842 | 34083 | 11759 (268) | 7 | $-16291.41 | -5.7% |
| **+20¢** | 40797 | 28415 | 12382 (334) | 7 | $-14693.32 | -5.7% |
| **+10¢ (15¢ stop)** | 89480 | 89268 | 212 (129) | 0 | $-33107.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 06:42 | +10 stop | DOGE | UP | 0.53 | 0.27 | -2.92 |
| 11-27 06:41 | +10 stop | DOGE | DOWN | 0.67 | 0.36 | -3.43 |
| 11-27 06:40 | +10 stop | DOGE | DOWN | 0.53 | 0.65 | 0.86 |
| 11-27 06:39 | +10 stop | BTC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-27 06:37 | +10 stop | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 11-27 06:37 | +10 | BNB | DOWN | 0.65 | 0.80 | 1.23 |
| 11-27 06:37 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.21 |
| 11-27 06:37 | +10 stop | DOGE | UP | 0.65 | 0.50 | -1.84 |
| 11-27 06:37 | +20 | DOGE | UP | 0.63 | open |  |
| 11-27 06:37 | +15 | DOGE | UP | 0.63 | open |  |
| 11-27 06:37 | +10 | DOGE | UP | 0.63 | open |  |
| 11-27 06:37 | +5 | DOGE | UP | 0.63 | open |  |
| 11-27 06:36 | +10 stop | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 11-27 06:36 | +10 stop | XRP | UP | 0.60 | 0.41 | -2.24 |
| 11-27 06:36 | +20 | XRP | UP | 0.61 | open |  |
| 11-27 06:36 | +15 | XRP | UP | 0.61 | open |  |
| 11-27 06:36 | +10 | XRP | UP | 0.61 | open |  |
| 11-27 06:36 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 11-27 06:36 | +10 stop | BTC | UP | 0.60 | 0.43 | -2.05 |
| 11-27 06:36 | +15 | BTC | UP | 0.60 | open |  |
| 11-27 06:36 | +10 | BTC | UP | 0.60 | open |  |
| 11-27 06:36 | +5 | BTC | UP | 0.60 | open |  |
| 11-27 06:35 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-27 06:35 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.41 |
| 11-27 06:35 | +10 stop | SOL | UP | 0.59 | 0.39 | -2.34 |
| 11-27 06:35 | +20 | SOL | UP | 0.59 | open |  |
| 11-27 06:35 | +15 | SOL | UP | 0.59 | open |  |
| 11-27 06:35 | +10 | SOL | UP | 0.59 | open |  |
| 11-27 06:35 | +5 | SOL | UP | 0.59 | open |  |
| 11-27 06:33 | +5 | BNB | UP | 0.69 | 0.74 | 0.21 |
| 11-27 06:33 | +5 | ZEC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-27 06:33 | +10 stop | HYPE | UP | 0.53 | 0.37 | -1.95 |
| 11-27 06:33 | +10 stop | XRP | UP | 0.63 | 0.75 | 0.86 |
| 11-27 06:33 | +10 | XRP | UP | 0.63 | 0.75 | 0.89 |
| 11-27 06:33 | +5 | XRP | UP | 0.63 | 0.70 | 0.38 |
| 11-27 06:33 | +5 | NEAR | DOWN | 0.57 | 0.66 | 0.56 |
| 11-27 06:32 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-27 06:32 | +20 | ZEC | DOWN | 0.71 | 0.95 | 2.26 |
| 11-27 06:32 | +15 | ZEC | DOWN | 0.71 | 0.89 | 1.58 |
| 11-27 06:32 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
