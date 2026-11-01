# Range-Scalp Bot

*Updated Sun Nov 01 23:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44046 | 38363 | 5683 (65) | 0 | $-12684.92 | -4.6% |
| **+10¢** | 32871 | 26307 | 6564 (86) | 1 | $-11415.00 | -5.5% |
| **+15¢** | 27508 | 20444 | 7064 (113) | 5 | $-10423.33 | -6.0% |
| **+20¢** | 24434 | 17037 | 7397 (147) | 6 | $-9182.45 | -6.0% |
| **+10¢ (15¢ stop)** | 53725 | 53639 | 86 (51) | 1 | $-20324.51 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 23:03 | +15 | BNB | UP | 0.65 | open |  |
| 11-01 23:03 | +10 stop | HYPE | UP | 0.68 | 0.80 | 0.92 |
| 11-01 23:03 | +10 stop | SOL | UP | 0.67 | 0.77 | 0.71 |
| 11-01 23:03 | +20 | SOL | UP | 0.67 | open |  |
| 11-01 23:03 | +15 | SOL | UP | 0.67 | 0.83 | 1.34 |
| 11-01 23:03 | +10 | SOL | UP | 0.67 | 0.77 | 0.71 |
| 11-01 23:03 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 11-01 23:03 | +10 stop | BNB | UP | 0.65 | 0.77 | 0.91 |
| 11-01 23:03 | +10 | BNB | UP | 0.65 | 0.77 | 0.91 |
| 11-01 23:03 | +5 | BNB | UP | 0.65 | 0.73 | 0.50 |
| 11-01 23:03 | +10 stop | ETH | UP | 0.68 | 0.82 | 1.13 |
| 11-01 23:03 | +10 stop | BTC | UP | 0.67 | open |  |
| 11-01 23:02 | +10 stop | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-01 23:02 | +20 | ZEC | UP | 0.71 | open |  |
| 11-01 23:02 | +15 | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-01 23:02 | +10 | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-01 23:02 | +5 | ZEC | UP | 0.71 | 0.78 | 0.42 |
| 11-01 23:02 | +10 stop | HYPE | DOWN | 0.49 | 0.64 | 1.15 |
| 11-01 23:02 | +10 stop | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-01 23:02 | +20 | BNB | UP | 0.48 | 0.73 | 2.18 |
| 11-01 23:02 | +15 | BNB | UP | 0.48 | 0.63 | 1.15 |
| 11-01 23:02 | +10 | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-01 23:02 | +5 | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-01 23:02 | +10 stop | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-01 23:02 | +20 | XRP | UP | 0.69 | open |  |
| 11-01 23:02 | +15 | XRP | UP | 0.69 | open |  |
| 11-01 23:02 | +10 | XRP | UP | 0.69 | 0.80 | 0.83 |
| 11-01 23:02 | +5 | XRP | UP | 0.69 | 0.77 | 0.52 |
| 11-01 23:02 | +10 stop | HYPE | UP | 0.69 | 0.36 | -3.62 |
| 11-01 23:02 | +20 | HYPE | UP | 0.69 | open |  |
| 11-01 23:02 | +15 | HYPE | UP | 0.69 | open |  |
| 11-01 23:02 | +10 | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 11-01 23:02 | +5 | HYPE | UP | 0.69 | 0.80 | 0.83 |
| 11-01 23:01 | +10 stop | BTC | UP | 0.69 | 0.53 | -1.93 |
| 11-01 23:01 | +20 | BTC | UP | 0.69 | open |  |
| 11-01 23:01 | +15 | BTC | UP | 0.69 | open |  |
| 11-01 23:01 | +10 | BTC | UP | 0.69 | open |  |
| 11-01 23:01 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 11-01 23:01 | +10 stop | ETH | UP | 0.67 | 0.51 | -1.94 |
| 11-01 23:01 | +20 | ETH | UP | 0.67 | open |  |
