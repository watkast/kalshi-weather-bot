# Range-Scalp Bot

*Updated Wed Oct 28 09:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37837 | 33018 | 4819 (46) | 2 | $-10622.97 | -4.5% |
| **+10¢** | 28245 | 22669 | 5576 (68) | 3 | $-9477.77 | -5.3% |
| **+15¢** | 23622 | 17634 | 5988 (93) | 4 | $-8445.23 | -5.7% |
| **+20¢** | 20948 | 14679 | 6269 (118) | 5 | $-7410.07 | -5.6% |
| **+10¢ (15¢ stop)** | 46345 | 46278 | 67 (35) | 0 | $-17640.08 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 09:10 | +10 stop | ZEC | UP | 0.54 | 0.68 | 1.06 |
| 10-28 09:09 | +10 stop | BTC | DOWN | 0.62 | 0.25 | -4.01 |
| 10-28 09:09 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-28 09:09 | +15 | BTC | DOWN | 0.62 | open |  |
| 10-28 09:09 | +10 | BTC | DOWN | 0.62 | open |  |
| 10-28 09:09 | +5 | BTC | DOWN | 0.62 | open |  |
| 10-28 09:09 | +10 stop | ZEC | DOWN | 0.60 | 0.37 | -2.64 |
| 10-28 09:09 | +5 | ZEC | DOWN | 0.61 | open |  |
| 10-28 09:06 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-28 09:06 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 10-28 09:06 | +5 | BTC | DOWN | 0.50 | 0.62 | 0.85 |
| 10-28 09:06 | +10 stop | SOL | DOWN | 0.61 | 0.78 | 1.40 |
| 10-28 09:05 | +10 stop | XRP | DOWN | 0.71 | 0.53 | -2.12 |
| 10-28 09:05 | +5 | DOGE | DOWN | 0.63 | 0.68 | 0.17 |
| 10-28 09:04 | +5 | BTC | DOWN | 0.49 | 0.56 | 0.34 |
| 10-28 09:04 | +5 | BTC | DOWN | 0.59 | 0.65 | 0.27 |
| 10-28 09:04 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-28 09:04 | +10 stop | XRP | DOWN | 0.70 | 0.52 | -2.13 |
| 10-28 09:04 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-28 09:04 | +10 stop | ZEC | DOWN | 0.62 | 0.72 | 0.70 |
| 10-28 09:04 | +10 stop | SOL | DOWN | 0.67 | 0.50 | -2.04 |
| 10-28 09:03 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.12 |
| 10-28 09:03 | +10 stop | SOL | UP | 0.40 | 0.54 | 1.05 |
| 10-28 09:03 | +5 | XRP | DOWN | 0.53 | 0.58 | 0.14 |
| 10-28 09:02 | +10 stop | ZEC | DOWN | 0.65 | 0.50 | -1.84 |
| 10-28 09:02 | +20 | ZEC | DOWN | 0.65 | open |  |
| 10-28 09:02 | +15 | ZEC | DOWN | 0.65 | open |  |
| 10-28 09:02 | +10 | ZEC | DOWN | 0.65 | open |  |
| 10-28 09:02 | +5 | ZEC | DOWN | 0.65 | 0.71 | 0.29 |
| 10-28 09:02 | +5 | SOL | DOWN | 0.53 | 0.66 | 0.96 |
| 10-28 09:02 | +5 | HYPE | UP | 0.58 | 0.79 | 1.83 |
| 10-28 09:02 | +10 stop | XRP | DOWN | 0.63 | 0.47 | -1.95 |
| 10-28 09:02 | +20 | XRP | DOWN | 0.63 | open |  |
| 10-28 09:02 | +15 | XRP | DOWN | 0.62 | open |  |
| 10-28 09:02 | +10 | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 10-28 09:02 | +5 | XRP | DOWN | 0.61 | 0.66 | 0.17 |
| 10-28 09:01 | +10 stop | HYPE | UP | 0.54 | 0.79 | 2.20 |
| 10-28 09:01 | +20 | HYPE | UP | 0.54 | 0.79 | 2.20 |
| 10-28 09:01 | +15 | HYPE | UP | 0.56 | 0.79 | 2.00 |
| 10-28 09:01 | +10 | HYPE | UP | 0.56 | 0.79 | 2.00 |
