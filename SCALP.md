# Range-Scalp Bot

*Updated Mon Nov 02 15:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45062 | 39232 | 5830 (67) | 1 | $-13075.38 | -4.6% |
| **+10¢** | 33638 | 26885 | 6753 (88) | 0 | $-11934.81 | -5.6% |
| **+15¢** | 28136 | 20870 | 7266 (115) | 0 | $-10986.01 | -6.2% |
| **+20¢** | 24988 | 17382 | 7606 (150) | 3 | $-9719.83 | -6.2% |
| **+10¢ (15¢ stop)** | 55009 | 54922 | 87 (51) | 0 | $-20836.35 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 15:23 | +5 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 15:22 | +15 | BTC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-02 15:22 | +10 stop | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 15:22 | +10 | BTC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-02 15:22 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-02 15:22 | +10 | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-02 15:22 | +5 | NEAR | DOWN | 0.55 | 0.60 | 0.15 |
| 11-02 15:22 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-02 15:22 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-02 15:22 | +15 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-02 15:22 | +10 | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-02 15:22 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-02 15:21 | +5 | ETH | DOWN | 0.71 | 0.76 | 0.22 |
| 11-02 15:21 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.68 |
| 11-02 15:21 | +15 | BNB | DOWN | 0.61 | 0.78 | 1.40 |
| 11-02 15:21 | +10 | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 11-02 15:21 | +5 | BNB | DOWN | 0.61 | 0.70 | 0.58 |
| 11-02 15:21 | +10 stop | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-02 15:21 | +10 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-02 15:21 | +5 | ZEC | DOWN | 0.68 | 0.83 | 1.24 |
| 11-02 15:21 | +15 | BTC | DOWN | 0.42 | 0.59 | 1.35 |
| 11-02 15:21 | +10 | BTC | DOWN | 0.42 | 0.54 | 0.84 |
| 11-02 15:21 | +10 stop | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 11-02 15:21 | +20 | NEAR | DOWN | 0.52 | 0.73 | 1.78 |
| 11-02 15:21 | +15 | NEAR | DOWN | 0.52 | 0.69 | 1.37 |
| 11-02 15:21 | +10 | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 11-02 15:21 | +5 | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 11-02 15:19 | +10 stop | BTC | DOWN | 0.64 | 0.48 | -1.95 |
| 11-02 15:18 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 15:18 | +5 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 15:18 | +5 | SOL | DOWN | 0.69 | 0.75 | 0.31 |
| 11-02 15:18 | +10 stop | ZEC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-02 15:18 | +10 stop | HYPE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-02 15:18 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 15:18 | +15 | DOGE | DOWN | 0.64 | 0.81 | 1.42 |
| 11-02 15:18 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 15:18 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 15:18 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 15:18 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 15:18 | +10 stop | NEAR | UP | 0.52 | 0.33 | -2.24 |
