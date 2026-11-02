# Range-Scalp Bot

*Updated Mon Nov 02 20:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45084 | 39253 | 5831 (67) | 0 | $-13064.78 | -4.6% |
| **+10¢** | 33655 | 26899 | 6756 (88) | 0 | $-11933.18 | -5.6% |
| **+15¢** | 28150 | 20881 | 7269 (115) | 0 | $-10984.15 | -6.2% |
| **+20¢** | 25000 | 17389 | 7611 (150) | 0 | $-9735.69 | -6.2% |
| **+10¢ (15¢ stop)** | 55030 | 54943 | 87 (51) | 0 | $-20833.56 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 20:38 | +10 stop | HYPE | DOWN | 0.57 | 0.74 | 1.34 |
| 11-02 20:38 | +20 | HYPE | DOWN | 0.57 | 0.87 | 2.74 |
| 11-02 20:38 | +15 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-02 20:38 | +10 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-02 20:38 | +5 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-02 20:37 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-02 20:37 | +10 | XRP | DOWN | 0.55 | 0.72 | 1.32 |
| 11-02 20:37 | +5 | XRP | DOWN | 0.55 | 0.65 | 0.61 |
| 11-02 20:35 | +10 stop | HYPE | UP | 0.54 | 0.72 | 1.47 |
| 11-02 20:35 | +20 | HYPE | UP | 0.54 | 0.76 | 1.89 |
| 11-02 20:35 | +15 | HYPE | UP | 0.53 | 0.72 | 1.57 |
| 11-02 20:35 | +10 | HYPE | UP | 0.53 | 0.72 | 1.57 |
| 11-02 20:35 | +5 | HYPE | UP | 0.53 | 0.61 | 0.45 |
| 11-02 20:34 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-02 20:34 | +15 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-02 20:34 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-02 20:34 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-02 20:34 | +10 stop | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-02 20:34 | +10 | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-02 20:34 | +5 | BTC | DOWN | 0.65 | 0.78 | 1.01 |
| 11-02 20:32 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-02 20:32 | +20 | BTC | DOWN | 0.62 | 0.83 | 1.83 |
| 11-02 20:32 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 11-02 20:32 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 11-02 20:32 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-02 20:32 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 20:32 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 11-02 20:32 | +15 | XRP | DOWN | 0.67 | 0.82 | 1.23 |
| 11-02 20:32 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-02 20:32 | +5 | XRP | DOWN | 0.67 | 0.74 | 0.40 |
| 11-02 20:32 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-02 20:32 | +20 | NEAR | DOWN | 0.66 | 0.90 | 2.17 |
| 11-02 20:32 | +15 | NEAR | DOWN | 0.66 | 0.83 | 1.44 |
| 11-02 20:32 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-02 20:32 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 11-02 15:28 | +5 | DOGE | DOWN | 0.36 | 0.57 | 1.75 |
| 11-02 15:28 | +10 stop | ZEC | UP | 0.66 | 0.95 | 2.71 |
| 11-02 15:28 | +5 | ZEC | UP | 0.69 | 0.95 | 2.42 |
| 11-02 15:28 | +10 stop | DOGE | DOWN | 0.58 | 0.31 | -3.02 |
| 11-02 15:28 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.26 |
