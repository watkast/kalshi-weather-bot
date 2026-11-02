# Range-Scalp Bot

*Updated Mon Nov 02 23:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45317 | 39456 | 5861 (67) | 5 | $-13118.42 | -4.6% |
| **+10¢** | 33822 | 27032 | 6790 (89) | 6 | $-11990.46 | -5.6% |
| **+15¢** | 28292 | 20985 | 7307 (116) | 6 | $-11045.58 | -6.2% |
| **+20¢** | 25124 | 17472 | 7652 (151) | 8 | $-9809.15 | -6.2% |
| **+10¢ (15¢ stop)** | 55291 | 55204 | 87 (51) | 1 | $-20892.31 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 23:55 | +10 stop | BTC | DOWN | 0.51 | 0.66 | 1.16 |
| 11-02 23:55 | +15 | BTC | DOWN | 0.51 | 0.66 | 1.16 |
| 11-02 23:55 | +10 | BTC | DOWN | 0.51 | 0.66 | 1.16 |
| 11-02 23:55 | +5 | BTC | DOWN | 0.51 | 0.66 | 1.16 |
| 11-02 23:54 | +10 stop | SOL | DOWN | 0.58 | open |  |
| 11-02 23:54 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-02 23:54 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-02 23:54 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-02 23:54 | +10 stop | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-02 23:53 | +10 stop | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-02 23:53 | +15 | XRP | UP | 0.59 | 0.82 | 2.02 |
| 11-02 23:53 | +10 | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-02 23:53 | +5 | XRP | UP | 0.59 | 0.70 | 0.78 |
| 11-02 23:53 | +10 stop | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 11-02 23:53 | +10 stop | NEAR | DOWN | 0.61 | 0.39 | -2.54 |
| 11-02 23:53 | +10 stop | ETH | DOWN | 0.54 | 0.27 | -3.02 |
| 11-02 23:53 | +10 stop | BNB | DOWN | 0.53 | 0.32 | -2.44 |
| 11-02 23:51 | +10 stop | ZEC | DOWN | 0.55 | 0.65 | 0.66 |
| 11-02 23:51 | +5 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-02 23:51 | +10 stop | BNB | UP | 0.66 | 0.44 | -2.54 |
| 11-02 23:50 | +10 stop | HYPE | UP | 0.69 | 0.49 | -2.33 |
| 11-02 23:50 | +5 | NEAR | UP | 0.58 | 0.71 | 0.97 |
| 11-02 23:50 | +10 stop | ETH | UP | 0.59 | 0.39 | -2.34 |
| 11-02 23:50 | +5 | NEAR | UP | 0.59 | 0.67 | 0.47 |
| 11-02 23:49 | +10 stop | ZEC | UP | 0.59 | 0.42 | -2.05 |
| 11-02 23:48 | +10 stop | HYPE | UP | 0.61 | 0.73 | 0.89 |
| 11-02 23:48 | +10 stop | NEAR | UP | 0.64 | 0.49 | -1.85 |
| 11-02 23:48 | +20 | NEAR | UP | 0.64 | open |  |
| 11-02 23:48 | +15 | NEAR | UP | 0.64 | open |  |
| 11-02 23:48 | +10 | NEAR | UP | 0.64 | open |  |
| 11-02 23:48 | +5 | NEAR | UP | 0.64 | 0.71 | 0.38 |
| 11-02 23:48 | +5 | SOL | DOWN | 0.69 | 0.74 | 0.21 |
| 11-02 23:48 | +5 | BNB | DOWN | 0.58 | open |  |
| 11-02 23:47 | +5 | ETH | DOWN | 0.59 | open |  |
| 11-02 23:46 | +10 stop | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-02 23:46 | +20 | DOGE | DOWN | 0.58 | 0.85 | 2.43 |
| 11-02 23:46 | +15 | DOGE | DOWN | 0.58 | 0.85 | 2.43 |
| 11-02 23:46 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-02 23:46 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-02 23:46 | +10 stop | ZEC | DOWN | 0.62 | 0.46 | -1.95 |
