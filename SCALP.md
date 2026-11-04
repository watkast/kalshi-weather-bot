# Range-Scalp Bot

*Updated Wed Nov 04 21:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47529 | 41385 | 6144 (73) | 3 | $-13709.60 | -4.6% |
| **+10¢** | 35511 | 28383 | 7128 (98) | 4 | $-12537.51 | -5.6% |
| **+15¢** | 29745 | 22069 | 7676 (126) | 4 | $-11496.48 | -6.2% |
| **+20¢** | 26429 | 18389 | 8040 (166) | 4 | $-10158.55 | -6.1% |
| **+10¢ (15¢ stop)** | 57930 | 57837 | 93 (56) | 3 | $-21585.65 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 21:02 | +5 | BTC | UP | 0.56 | open |  |
| 11-04 21:01 | +10 stop | BTC | UP | 0.54 | open |  |
| 11-04 21:01 | +20 | BTC | UP | 0.54 | open |  |
| 11-04 21:01 | +15 | BTC | UP | 0.54 | open |  |
| 11-04 21:01 | +10 | BTC | UP | 0.54 | open |  |
| 11-04 21:01 | +5 | BTC | UP | 0.54 | 0.59 | 0.15 |
| 11-04 21:01 | +10 stop | ZEC | UP | 0.68 | 0.50 | -2.14 |
| 11-04 21:01 | +20 | ZEC | UP | 0.68 | open |  |
| 11-04 21:01 | +15 | ZEC | UP | 0.68 | open |  |
| 11-04 21:01 | +10 | ZEC | UP | 0.68 | open |  |
| 11-04 21:01 | +5 | ZEC | UP | 0.68 | 0.76 | 0.51 |
| 11-04 21:01 | +10 stop | XRP | UP | 0.65 | open |  |
| 11-04 21:01 | +20 | XRP | UP | 0.65 | open |  |
| 11-04 21:01 | +15 | XRP | UP | 0.65 | open |  |
| 11-04 21:01 | +10 | XRP | UP | 0.65 | open |  |
| 11-04 21:01 | +5 | XRP | UP | 0.65 | open |  |
| 11-04 21:01 | +10 stop | SOL | UP | 0.62 | open |  |
| 11-04 21:01 | +20 | SOL | UP | 0.62 | open |  |
| 11-04 21:01 | +15 | SOL | UP | 0.62 | open |  |
| 11-04 21:01 | +10 | SOL | UP | 0.62 | open |  |
| 11-04 21:01 | +5 | SOL | UP | 0.62 | open |  |
| 11-04 20:59 | +10 stop | BTC | DOWN | 0.71 | 0.87 | 1.37 |
| 11-04 20:59 | +20 | BTC | DOWN | 0.71 | 1.00 | 2.71 |
| 11-04 20:59 | +15 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-04 20:59 | +10 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-04 20:59 | +5 | BTC | DOWN | 0.69 | 0.87 | 1.57 |
| 11-04 20:57 | +10 stop | ZEC | DOWN | 0.70 | 0.90 | 1.82 |
| 11-04 20:57 | +20 | ZEC | DOWN | 0.70 | 0.90 | 1.82 |
| 11-04 20:57 | +15 | ZEC | DOWN | 0.70 | 0.90 | 1.82 |
| 11-04 20:57 | +10 | ZEC | DOWN | 0.70 | 0.90 | 1.82 |
| 11-04 20:57 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-04 20:52 | +10 stop | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 11-04 20:51 | +10 stop | NEAR | UP | 0.55 | 0.26 | -3.22 |
| 11-04 20:50 | +5 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-04 20:50 | +10 stop | NEAR | UP | 0.42 | 0.54 | 0.84 |
| 11-04 20:49 | +5 | BNB | DOWN | 0.58 | 0.65 | 0.32 |
| 11-04 20:49 | +5 | SOL | DOWN | 0.52 | 0.64 | 0.85 |
| 11-04 20:48 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-04 20:48 | +20 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 11-04 20:48 | +15 | BTC | DOWN | 0.63 | 0.79 | 1.31 |
