# Range-Scalp Bot

*Updated Mon Nov 02 14:13 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44973 | 39162 | 5811 (66) | 3 | $-12997.81 | -4.6% |
| **+10¢** | 33571 | 26836 | 6735 (87) | 4 | $-11878.64 | -5.6% |
| **+15¢** | 28075 | 20826 | 7249 (114) | 2 | $-10952.72 | -6.2% |
| **+20¢** | 24941 | 17352 | 7589 (149) | 2 | $-9684.88 | -6.2% |
| **+10¢ (15¢ stop)** | 54897 | 54810 | 87 (51) | 0 | $-20781.45 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 14:13 | +5 | ETH | DOWN | 0.39 | 0.64 | 2.16 |
| 11-02 14:13 | +10 stop | ETH | DOWN | 0.39 | 0.64 | 2.16 |
| 11-02 14:12 | +5 | ZEC | UP | 0.58 | open |  |
| 11-02 14:11 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 11-02 14:11 | +5 | BTC | DOWN | 0.69 | 0.77 | 0.52 |
| 11-02 14:11 | +10 stop | BNB | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 14:11 | +5 | BNB | DOWN | 0.51 | 0.68 | 1.36 |
| 11-02 14:11 | +10 stop | BTC | DOWN | 0.64 | 0.77 | 1.00 |
| 11-02 14:10 | +10 stop | ZEC | UP | 0.55 | 0.27 | -3.12 |
| 11-02 14:10 | +10 | ZEC | UP | 0.55 | open |  |
| 11-02 14:10 | +5 | ZEC | UP | 0.55 | 0.62 | 0.35 |
| 11-02 14:10 | +10 stop | BNB | UP | 0.52 | 0.30 | -2.53 |
| 11-02 14:10 | +10 | BNB | UP | 0.52 | open |  |
| 11-02 14:10 | +5 | BNB | UP | 0.53 | 0.61 | 0.45 |
| 11-02 14:10 | +10 stop | SOL | UP | 0.52 | 0.23 | -3.21 |
| 11-02 14:10 | +10 stop | DOGE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-02 14:09 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 11-02 14:08 | +10 stop | SOL | DOWN | 0.61 | 0.44 | -2.05 |
| 11-02 14:08 | +10 stop | HYPE | DOWN | 0.62 | 0.83 | 1.83 |
| 11-02 14:08 | +10 stop | BTC | UP | 0.66 | 0.79 | 1.02 |
| 11-02 14:08 | +5 | BNB | UP | 0.69 | 0.76 | 0.42 |
| 11-02 14:08 | +10 stop | DOGE | DOWN | 0.70 | 0.54 | -1.93 |
| 11-02 14:08 | +10 stop | NEAR | DOWN | 0.63 | 0.80 | 1.41 |
| 11-02 14:07 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 11-02 14:07 | +10 | BNB | UP | 0.59 | 0.70 | 0.78 |
| 11-02 14:07 | +5 | BNB | UP | 0.59 | 0.66 | 0.37 |
| 11-02 14:07 | +10 stop | SOL | UP | 0.62 | 0.47 | -1.85 |
| 11-02 14:07 | +10 stop | DOGE | UP | 0.59 | 0.42 | -2.05 |
| 11-02 14:06 | +10 stop | HYPE | UP | 0.50 | 0.34 | -1.94 |
| 11-02 14:06 | +10 stop | XRP | UP | 0.61 | 0.46 | -1.85 |
| 11-02 14:06 | +10 stop | NEAR | UP | 0.57 | 0.40 | -2.05 |
| 11-02 14:06 | +5 | HYPE | UP | 0.56 | open |  |
| 11-02 14:06 | +10 stop | DOGE | UP | 0.69 | 0.54 | -1.83 |
| 11-02 14:05 | +10 stop | BTC | UP | 0.61 | 0.71 | 0.68 |
| 11-02 14:05 | +10 stop | BNB | UP | 0.58 | 0.69 | 0.77 |
| 11-02 14:05 | +10 stop | SOL | DOWN | 0.55 | 0.27 | -3.12 |
| 11-02 14:05 | +15 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-02 14:05 | +10 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-02 14:05 | +5 | SOL | DOWN | 0.55 | 0.76 | 1.79 |
| 11-02 14:05 | +10 stop | HYPE | DOWN | 0.69 | 0.45 | -2.77 |
