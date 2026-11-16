# Range-Scalp Bot

*Updated Mon Nov 16 23:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62406 | 54447 | 7959 (117) | 2 | $-16877.88 | -4.3% |
| **+10¢** | 46603 | 37290 | 9313 (159) | 4 | $-15751.03 | -5.4% |
| **+15¢** | 39051 | 29005 | 10046 (201) | 4 | $-14327.28 | -5.8% |
| **+20¢** | 34802 | 24265 | 10537 (256) | 4 | $-12529.00 | -5.7% |
| **+10¢ (15¢ stop)** | 75956 | 75800 | 156 (92) | 0 | $-28033.61 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 23:11 | +10 stop | DOGE | UP | 0.69 | 0.43 | -2.93 |
| 11-16 23:10 | +10 stop | ZEC | UP | 0.67 | 0.79 | 0.92 |
| 11-16 23:10 | +10 stop | SOL | UP | 0.63 | 0.80 | 1.41 |
| 11-16 23:10 | +5 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-16 23:08 | +10 stop | BTC | DOWN | 0.65 | 0.45 | -2.34 |
| 11-16 23:08 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-16 23:08 | +10 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-16 23:08 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-16 23:08 | +10 stop | ZEC | DOWN | 0.59 | 0.39 | -2.34 |
| 11-16 23:08 | +10 stop | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-16 23:08 | +20 | BTC | DOWN | 0.54 | 0.74 | 1.68 |
| 11-16 23:08 | +15 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 11-16 23:08 | +10 | BTC | DOWN | 0.52 | 0.69 | 1.37 |
| 11-16 23:08 | +5 | BTC | DOWN | 0.50 | 0.69 | 1.57 |
| 11-16 23:08 | +10 stop | ETH | DOWN | 0.46 | 0.29 | -2.03 |
| 11-16 23:08 | +20 | ETH | DOWN | 0.47 | open |  |
| 11-16 23:08 | +15 | ETH | DOWN | 0.47 | open |  |
| 11-16 23:07 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-16 23:07 | +10 stop | ZEC | DOWN | 0.71 | 0.55 | -1.93 |
| 11-16 23:07 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-16 23:07 | +15 | ZEC | DOWN | 0.69 | open |  |
| 11-16 23:07 | +10 | ZEC | DOWN | 0.69 | open |  |
| 11-16 23:07 | +5 | ZEC | DOWN | 0.69 | open |  |
| 11-16 23:06 | +10 | ETH | DOWN | 0.71 | open |  |
| 11-16 23:06 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-16 23:06 | +10 stop | DOGE | DOWN | 0.71 | 0.51 | -2.33 |
| 11-16 23:06 | +20 | DOGE | DOWN | 0.71 | 0.94 | 2.16 |
| 11-16 23:06 | +15 | DOGE | DOWN | 0.71 | 0.94 | 2.16 |
| 11-16 23:06 | +10 | DOGE | DOWN | 0.71 | 0.94 | 2.16 |
| 11-16 23:06 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-16 23:06 | +10 stop | SOL | DOWN | 0.62 | 0.38 | -2.74 |
| 11-16 23:06 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-16 23:06 | +10 | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 11-16 23:06 | +5 | SOL | DOWN | 0.62 | 0.69 | 0.38 |
| 11-16 23:04 | +10 stop | HYPE | UP | 0.67 | 0.89 | 1.97 |
| 11-16 23:04 | +10 stop | NEAR | DOWN | 0.68 | 0.48 | -2.34 |
| 11-16 23:04 | +10 | NEAR | DOWN | 0.67 | open |  |
| 11-16 23:04 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-16 23:03 | +5 | NEAR | DOWN | 0.62 | 0.68 | 0.27 |
| 11-16 23:02 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
