# Range-Scalp Bot

*Updated Thu Oct 08 00:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7003 | 6077 | 926 (13) | 3 | $-2105.90 | -4.8% |
| **+10¢** | 5310 | 4228 | 1082 (20) | 3 | $-1980.25 | -5.9% |
| **+15¢** | 4457 | 3317 | 1140 (27) | 3 | $-1618.43 | -5.8% |
| **+20¢** | 3980 | 2792 | 1188 (34) | 3 | $-1284.24 | -5.1% |
| **+10¢ (15¢ stop)** | 8479 | 8457 | 22 (14) | 1 | $-2992.07 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 00:09 | +10 stop | NEAR | UP | 0.57 | open |  |
| 10-08 00:08 | +10 stop | NEAR | UP | 0.53 | 0.63 | 0.65 |
| 10-08 00:07 | +10 stop | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-08 00:07 | +20 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 10-08 00:07 | +15 | SOL | DOWN | 0.63 | 0.86 | 2.04 |
| 10-08 00:07 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-08 00:07 | +5 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 10-08 00:06 | +10 stop | ZEC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-08 00:06 | +20 | ZEC | DOWN | 0.67 | open |  |
| 10-08 00:06 | +15 | ZEC | DOWN | 0.67 | open |  |
| 10-08 00:06 | +10 | ZEC | DOWN | 0.68 | open |  |
| 10-08 00:06 | +5 | ZEC | DOWN | 0.69 | open |  |
| 10-08 00:06 | +10 stop | NEAR | DOWN | 0.54 | 0.37 | -2.05 |
| 10-08 00:04 | +15 | XRP | DOWN | 0.70 | 0.85 | 1.26 |
| 10-08 00:04 | +5 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-08 00:04 | +5 | NEAR | UP | 0.68 | open |  |
| 10-08 00:03 | +10 stop | BNB | UP | 0.61 | 0.92 | 2.87 |
| 10-08 00:02 | +10 stop | XRP | DOWN | 0.69 | 0.81 | 0.94 |
| 10-08 00:02 | +10 | XRP | DOWN | 0.70 | 0.81 | 0.84 |
| 10-08 00:02 | +5 | XRP | DOWN | 0.68 | 0.76 | 0.51 |
| 10-08 00:02 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 10-08 00:01 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-08 00:01 | +20 | XRP | DOWN | 0.58 | 0.81 | 2.00 |
| 10-08 00:01 | +15 | XRP | DOWN | 0.58 | 0.76 | 1.49 |
| 10-08 00:01 | +10 | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 10-08 00:01 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.46 |
| 10-08 00:01 | +10 stop | NEAR | UP | 0.66 | 0.48 | -2.14 |
| 10-08 00:01 | +20 | NEAR | UP | 0.66 | open |  |
| 10-08 00:01 | +15 | NEAR | UP | 0.66 | open |  |
| 10-08 00:01 | +10 | NEAR | UP | 0.66 | open |  |
| 10-08 00:01 | +5 | NEAR | UP | 0.66 | 0.73 | 0.40 |
| 10-08 00:01 | +10 stop | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-08 00:01 | +20 | HYPE | DOWN | 0.58 | 0.78 | 1.69 |
| 10-08 00:01 | +15 | HYPE | DOWN | 0.58 | 0.77 | 1.59 |
| 10-08 00:01 | +10 | HYPE | DOWN | 0.58 | 0.70 | 0.87 |
| 10-08 00:01 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-08 00:01 | +10 stop | BTC | DOWN | 0.66 | 0.78 | 0.91 |
| 10-08 00:01 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-08 00:01 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-08 00:01 | +10 | BTC | DOWN | 0.66 | 0.78 | 0.91 |
