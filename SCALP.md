# Range-Scalp Bot

*Updated Mon Nov 02 04:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44381 | 38649 | 5732 (65) | 5 | $-12829.42 | -4.6% |
| **+10¢** | 33124 | 26498 | 6626 (86) | 7 | $-11594.04 | -5.6% |
| **+15¢** | 27730 | 20599 | 7131 (113) | 8 | $-10592.72 | -6.1% |
| **+20¢** | 24642 | 17179 | 7463 (147) | 8 | $-9292.57 | -6.0% |
| **+10¢ (15¢ stop)** | 54174 | 54088 | 86 (51) | 0 | $-20582.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 04:25 | +10 stop | NEAR | DOWN | 0.64 | 0.77 | 1.00 |
| 11-02 04:25 | +5 | NEAR | DOWN | 0.68 | 0.77 | 0.61 |
| 11-02 04:25 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 04:24 | +10 | NEAR | UP | 0.48 | open |  |
| 11-02 04:24 | +5 | NEAR | UP | 0.48 | 0.56 | 0.44 |
| 11-02 04:24 | +10 stop | HYPE | UP | 0.54 | 0.21 | -3.64 |
| 11-02 04:24 | +20 | HYPE | UP | 0.56 | open |  |
| 11-02 04:24 | +10 | HYPE | UP | 0.57 | open |  |
| 11-02 04:24 | +5 | HYPE | UP | 0.57 | open |  |
| 11-02 04:24 | +5 | ZEC | DOWN | 0.60 | 0.75 | 1.20 |
| 11-02 04:23 | +10 stop | BTC | DOWN | 0.65 | 0.89 | 2.17 |
| 11-02 04:23 | +10 stop | ETH | DOWN | 0.59 | 0.69 | 0.68 |
| 11-02 04:23 | +10 stop | BNB | UP | 0.52 | 0.25 | -3.06 |
| 11-02 04:22 | +10 stop | SOL | UP | 0.58 | 0.17 | -4.38 |
| 11-02 04:22 | +10 stop | ZEC | UP | 0.49 | 0.23 | -2.91 |
| 11-02 04:22 | +5 | ZEC | UP | 0.50 | 0.55 | 0.14 |
| 11-02 04:21 | +10 stop | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-02 04:21 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 11-02 04:21 | +15 | XRP | DOWN | 0.66 | 0.82 | 1.33 |
| 11-02 04:21 | +10 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-02 04:21 | +5 | XRP | DOWN | 0.66 | 0.78 | 0.91 |
| 11-02 04:21 | +10 stop | HYPE | UP | 0.69 | 0.81 | 0.90 |
| 11-02 04:21 | +15 | HYPE | UP | 0.69 | open |  |
| 11-02 04:21 | +10 | HYPE | UP | 0.69 | 0.81 | 0.90 |
| 11-02 04:21 | +5 | HYPE | UP | 0.69 | 0.77 | 0.48 |
| 11-02 04:20 | +10 stop | ZEC | UP | 0.44 | 0.56 | 0.84 |
| 11-02 04:20 | +20 | ZEC | UP | 0.45 | open |  |
| 11-02 04:20 | +15 | ZEC | UP | 0.47 | open |  |
| 11-02 04:20 | +10 | ZEC | UP | 0.47 | open |  |
| 11-02 04:20 | +5 | ZEC | UP | 0.47 | 0.56 | 0.55 |
| 11-02 04:20 | +10 stop | DOGE | DOWN | 0.67 | 0.52 | -1.84 |
| 11-02 04:20 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-02 04:20 | +10 | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 04:20 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-02 04:20 | +10 stop | NEAR | UP | 0.68 | 0.42 | -2.94 |
| 11-02 04:20 | +10 stop | BNB | UP | 0.48 | 0.58 | 0.64 |
| 11-02 04:19 | +10 stop | SOL | DOWN | 0.63 | 0.43 | -2.35 |
| 11-02 04:19 | +10 stop | BTC | DOWN | 0.65 | 0.48 | -2.04 |
| 11-02 04:19 | +5 | BNB | UP | 0.56 | open |  |
| 11-02 04:19 | +10 stop | HYPE | DOWN | 0.62 | 0.27 | -3.81 |
