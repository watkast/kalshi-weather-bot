# Range-Scalp Bot

*Updated Fri Nov 06 03:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49116 | 42796 | 6320 (75) | 1 | $-13943.30 | -4.5% |
| **+10¢** | 36673 | 29326 | 7347 (101) | 1 | $-12808.78 | -5.6% |
| **+15¢** | 30717 | 22806 | 7911 (130) | 1 | $-11687.47 | -6.1% |
| **+20¢** | 27303 | 19012 | 8291 (170) | 1 | $-10335.65 | -6.0% |
| **+10¢ (15¢ stop)** | 59907 | 59812 | 95 (57) | 0 | $-22201.97 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 03:40 | +10 stop | BNB | DOWN | 0.61 | 0.42 | -2.25 |
| 11-06 03:39 | +10 stop | BNB | DOWN | 0.68 | 0.37 | -3.43 |
| 11-06 03:39 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-06 03:39 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-06 03:39 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-06 03:39 | +5 | BNB | DOWN | 0.70 | open |  |
| 11-06 03:31 | +10 stop | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 03:31 | +20 | XRP | DOWN | 0.68 | 0.90 | 2.00 |
| 11-06 03:31 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 03:31 | +10 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 03:31 | +5 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 03:31 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-06 03:31 | +20 | HYPE | DOWN | 0.67 | 0.89 | 1.97 |
| 11-06 03:31 | +15 | HYPE | DOWN | 0.67 | 0.83 | 1.34 |
| 11-06 03:31 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-06 03:31 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-06 03:31 | +10 stop | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-06 03:31 | +20 | BTC | DOWN | 0.70 | 0.91 | 1.87 |
| 11-06 03:31 | +15 | BTC | DOWN | 0.70 | 0.88 | 1.57 |
| 11-06 03:31 | +10 | BTC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-06 03:31 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 03:28 | +10 stop | DOGE | DOWN | 0.66 | 0.96 | 2.83 |
| 11-06 03:28 | +10 | DOGE | DOWN | 0.68 | 0.96 | 2.63 |
| 11-06 03:28 | +5 | DOGE | DOWN | 0.68 | 0.96 | 2.63 |
| 11-06 03:26 | +10 stop | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-06 03:26 | +20 | ZEC | DOWN | 0.65 | 0.88 | 2.06 |
| 11-06 03:26 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-06 03:26 | +10 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 11-06 03:26 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-06 03:24 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-06 03:24 | +10 stop | NEAR | DOWN | 0.64 | 0.76 | 0.90 |
| 11-06 03:23 | +10 stop | DOGE | UP | 0.69 | 0.49 | -2.33 |
| 11-06 03:22 | +10 stop | NEAR | UP | 0.53 | 0.70 | 1.37 |
| 11-06 03:22 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.14 |
| 11-06 03:22 | +10 stop | DOGE | UP | 0.48 | 0.58 | 0.64 |
| 11-06 03:22 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 11-06 03:22 | +10 stop | SOL | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 03:22 | +20 | SOL | DOWN | 0.58 | 0.79 | 1.80 |
| 11-06 03:22 | +15 | SOL | DOWN | 0.58 | 0.73 | 1.18 |
| 11-06 03:22 | +10 | SOL | DOWN | 0.58 | 0.69 | 0.77 |
