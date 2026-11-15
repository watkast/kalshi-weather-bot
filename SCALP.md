# Range-Scalp Bot

*Updated Sun Nov 15 07:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60585 | 52855 | 7730 (107) | 4 | $-16442.43 | -4.3% |
| **+10¢** | 45259 | 36201 | 9058 (143) | 6 | $-15512.40 | -5.5% |
| **+15¢** | 37909 | 28137 | 9772 (181) | 7 | $-14194.01 | -6.0% |
| **+20¢** | 33788 | 23538 | 10250 (233) | 8 | $-12480.74 | -5.9% |
| **+10¢ (15¢ stop)** | 73744 | 73601 | 143 (82) | 0 | $-27137.75 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 07:58 | +10 stop | NEAR | DOWN | 0.52 | 0.02 | -5.17 |
| 11-15 07:58 | +15 | NEAR | DOWN | 0.52 | open |  |
| 11-15 07:58 | +10 | NEAR | DOWN | 0.52 | open |  |
| 11-15 07:58 | +5 | NEAR | DOWN | 0.52 | 0.57 | 0.14 |
| 11-15 07:57 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 11-15 07:57 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-15 07:57 | +10 stop | XRP | UP | 0.62 | 0.40 | -2.54 |
| 11-15 07:57 | +5 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 11-15 07:57 | +10 stop | ZEC | UP | 0.64 | 0.37 | -3.04 |
| 11-15 07:56 | +10 stop | ETH | UP | 0.70 | 0.82 | 0.94 |
| 11-15 07:56 | +20 | ETH | UP | 0.71 | 0.97 | 2.41 |
| 11-15 07:56 | +15 | ETH | UP | 0.71 | 0.86 | 1.26 |
| 11-15 07:56 | +10 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-15 07:56 | +5 | ETH | UP | 0.71 | 0.82 | 0.84 |
| 11-15 07:56 | +5 | BNB | DOWN | 0.51 | 0.61 | 0.65 |
| 11-15 07:56 | +10 stop | XRP | DOWN | 0.41 | 0.52 | 0.75 |
| 11-15 07:56 | +10 stop | NEAR | DOWN | 0.68 | 0.53 | -1.84 |
| 11-15 07:56 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-15 07:56 | +5 | ZEC | DOWN | 0.68 | open |  |
| 11-15 07:55 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-15 07:55 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-15 07:55 | +10 stop | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 07:55 | +20 | DOGE | DOWN | 0.66 | open |  |
| 11-15 07:55 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 07:55 | +10 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-15 07:55 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-15 07:55 | +10 stop | SOL | UP | 0.59 | 0.71 | 0.88 |
| 11-15 07:55 | +10 stop | HYPE | UP | 0.65 | 0.36 | -3.23 |
| 11-15 07:55 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 07:55 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 07:55 | +5 | BNB | DOWN | 0.62 | 0.68 | 0.27 |
| 11-15 07:54 | +10 | XRP | DOWN | 0.70 | open |  |
| 11-15 07:54 | +5 | XRP | DOWN | 0.69 | open |  |
| 11-15 07:54 | +10 stop | XRP | DOWN | 0.71 | 0.45 | -2.91 |
| 11-15 07:54 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-15 07:54 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-15 07:54 | +10 stop | BTC | DOWN | 0.65 | 0.45 | -2.34 |
| 11-15 07:54 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-15 07:54 | +10 | BTC | DOWN | 0.65 | open |  |
| 11-15 07:54 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
