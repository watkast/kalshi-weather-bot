# Range-Scalp Bot

*Updated Sat Oct 31 16:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42446 | 37027 | 5419 (59) | 3 | $-11915.31 | -4.5% |
| **+10¢** | 31646 | 25372 | 6274 (81) | 4 | $-10712.22 | -5.4% |
| **+15¢** | 26467 | 19702 | 6765 (109) | 4 | $-9805.76 | -5.9% |
| **+20¢** | 23504 | 16413 | 7091 (141) | 6 | $-8680.25 | -5.9% |
| **+10¢ (15¢ stop)** | 51764 | 51685 | 79 (44) | 1 | $-19561.80 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 16:07 | +10 stop | ZEC | UP | 0.68 | 0.49 | -2.24 |
| 10-31 16:06 | +10 stop | XRP | UP | 0.62 | 0.79 | 1.41 |
| 10-31 16:06 | +5 | XRP | UP | 0.62 | 0.79 | 1.41 |
| 10-31 16:06 | +10 stop | ZEC | UP | 0.63 | 0.73 | 0.69 |
| 10-31 16:05 | +5 | XRP | UP | 0.52 | 0.58 | 0.24 |
| 10-31 16:05 | +10 stop | NEAR | UP | 0.69 | open |  |
| 10-31 16:04 | +10 stop | NEAR | DOWN | 0.50 | 0.29 | -2.43 |
| 10-31 16:03 | +5 | XRP | UP | 0.63 | 0.68 | 0.17 |
| 10-31 16:03 | +10 stop | ZEC | UP | 0.70 | 0.80 | 0.73 |
| 10-31 16:03 | +10 stop | SOL | UP | 0.69 | 0.82 | 1.04 |
| 10-31 16:03 | +20 | SOL | UP | 0.69 | 0.91 | 2.03 |
| 10-31 16:03 | +15 | SOL | UP | 0.69 | 0.84 | 1.25 |
| 10-31 16:03 | +10 | SOL | UP | 0.69 | 0.82 | 1.04 |
| 10-31 16:03 | +5 | SOL | UP | 0.69 | 0.78 | 0.62 |
| 10-31 16:02 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
| 10-31 16:02 | +10 stop | NEAR | UP | 0.60 | 0.39 | -2.44 |
| 10-31 16:02 | +10 stop | BNB | UP | 0.61 | 0.73 | 0.89 |
| 10-31 16:02 | +15 | DOGE | UP | 0.71 | 0.86 | 1.26 |
| 10-31 16:02 | +10 | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-31 16:02 | +5 | DOGE | UP | 0.71 | 0.82 | 0.84 |
| 10-31 16:02 | +10 stop | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-31 16:02 | +20 | HYPE | UP | 0.70 | open |  |
| 10-31 16:02 | +15 | HYPE | UP | 0.70 | 0.87 | 1.47 |
| 10-31 16:02 | +10 | HYPE | UP | 0.70 | 0.80 | 0.73 |
| 10-31 16:02 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 10-31 16:02 | +10 stop | XRP | UP | 0.66 | 0.43 | -2.64 |
| 10-31 16:02 | +20 | XRP | UP | 0.66 | open |  |
| 10-31 16:02 | +15 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 10-31 16:02 | +10 | XRP | UP | 0.66 | 0.79 | 1.02 |
| 10-31 16:02 | +5 | XRP | UP | 0.66 | 0.75 | 0.60 |
| 10-31 16:01 | +10 stop | ETH | UP | 0.63 | 0.75 | 0.89 |
| 10-31 16:01 | +20 | ETH | UP | 0.63 | 0.84 | 1.83 |
| 10-31 16:01 | +15 | ETH | UP | 0.63 | 0.82 | 1.62 |
| 10-31 16:01 | +10 | ETH | UP | 0.64 | 0.75 | 0.79 |
| 10-31 16:01 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 10-31 16:01 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 10-31 16:01 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-31 16:01 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-31 16:01 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-31 16:01 | +5 | BTC | DOWN | 0.61 | open |  |
