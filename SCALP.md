# Range-Scalp Bot

*Updated Fri Nov 20 16:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66363 | 57914 | 8449 (128) | 2 | $-17871.27 | -4.3% |
| **+10¢** | 49546 | 39668 | 9878 (170) | 2 | $-16643.44 | -5.3% |
| **+15¢** | 41548 | 30896 | 10652 (217) | 3 | $-14976.64 | -5.7% |
| **+20¢** | 36995 | 25808 | 11187 (273) | 4 | $-13267.57 | -5.7% |
| **+10¢ (15¢ stop)** | 80811 | 80645 | 166 (100) | 0 | $-29836.98 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 16:02 | +10 stop | NEAR | DOWN | 0.69 | 0.80 | 0.83 |
| 11-20 16:02 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-20 16:02 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-20 16:02 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-20 16:02 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 11-20 16:02 | +5 | ZEC | UP | 0.62 | open |  |
| 11-20 16:02 | +5 | BNB | DOWN | 0.54 | 0.60 | 0.25 |
| 11-20 16:01 | +10 stop | SOL | DOWN | 0.57 | 0.72 | 1.18 |
| 11-20 16:01 | +20 | SOL | DOWN | 0.56 | open |  |
| 11-20 16:01 | +15 | SOL | DOWN | 0.55 | 0.72 | 1.37 |
| 11-20 16:01 | +10 | SOL | DOWN | 0.55 | 0.72 | 1.37 |
| 11-20 16:01 | +5 | SOL | DOWN | 0.54 | 0.72 | 1.47 |
| 11-20 16:01 | +10 stop | BTC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-20 16:01 | +20 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-20 16:01 | +15 | BTC | DOWN | 0.61 | 0.82 | 1.82 |
| 11-20 16:01 | +10 | BTC | DOWN | 0.61 | 0.74 | 0.99 |
| 11-20 16:01 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 11-20 16:01 | +10 stop | ETH | DOWN | 0.60 | 0.79 | 1.61 |
| 11-20 16:01 | +10 | ETH | DOWN | 0.60 | 0.79 | 1.61 |
| 11-20 16:01 | +5 | ETH | DOWN | 0.60 | 0.65 | 0.17 |
| 11-20 16:01 | +10 stop | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-20 16:01 | +20 | DOGE | DOWN | 0.56 | 0.82 | 2.31 |
| 11-20 16:01 | +15 | DOGE | DOWN | 0.56 | 0.82 | 2.31 |
| 11-20 16:01 | +10 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-20 16:01 | +5 | DOGE | DOWN | 0.56 | 0.66 | 0.66 |
| 11-20 16:01 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 11-20 16:01 | +20 | BNB | DOWN | 0.59 | 0.83 | 2.13 |
| 11-20 16:01 | +15 | BNB | DOWN | 0.59 | 0.74 | 1.19 |
| 11-20 16:01 | +10 | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 11-20 16:01 | +5 | BNB | DOWN | 0.59 | 0.65 | 0.27 |
| 11-20 16:01 | +10 stop | ZEC | UP | 0.54 | 0.33 | -2.44 |
| 11-20 16:01 | +20 | ZEC | UP | 0.54 | open |  |
| 11-20 16:01 | +15 | ZEC | UP | 0.54 | open |  |
| 11-20 16:01 | +10 | ZEC | UP | 0.54 | open |  |
| 11-20 16:01 | +5 | ZEC | UP | 0.54 | 0.62 | 0.45 |
| 11-20 16:00 | +10 stop | XRP | UP | 0.58 | 0.40 | -2.15 |
| 11-20 16:00 | +20 | XRP | UP | 0.59 | open |  |
| 11-20 16:00 | +15 | XRP | UP | 0.59 | open |  |
| 11-20 16:00 | +10 | XRP | UP | 0.59 | open |  |
| 11-20 16:00 | +5 | XRP | UP | 0.59 | open |  |
