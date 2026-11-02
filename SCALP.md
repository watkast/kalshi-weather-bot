# Range-Scalp Bot

*Updated Mon Nov 02 13:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44905 | 39102 | 5803 (66) | 1 | $-12986.51 | -4.6% |
| **+10¢** | 33521 | 26797 | 6724 (87) | 1 | $-11852.41 | -5.6% |
| **+15¢** | 28037 | 20801 | 7236 (114) | 2 | $-10909.22 | -6.2% |
| **+20¢** | 24909 | 17334 | 7575 (149) | 2 | $-9637.52 | -6.2% |
| **+10¢ (15¢ stop)** | 54805 | 54718 | 87 (51) | 0 | $-20714.33 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 13:10 | +10 stop | ZEC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-02 13:09 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-02 13:08 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 13:08 | +10 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 13:08 | +5 | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-02 13:08 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 13:08 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 13:08 | +5 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 11-02 13:08 | +10 stop | NEAR | UP | 0.64 | 0.42 | -2.55 |
| 11-02 13:08 | +15 | NEAR | UP | 0.64 | open |  |
| 11-02 13:08 | +10 | NEAR | UP | 0.64 | open |  |
| 11-02 13:08 | +5 | NEAR | UP | 0.64 | open |  |
| 11-02 13:07 | +5 | BTC | DOWN | 0.68 | 0.81 | 1.03 |
| 11-02 13:06 | +10 stop | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 11-02 13:06 | +10 | BTC | DOWN | 0.63 | 0.81 | 1.52 |
| 11-02 13:06 | +5 | BTC | DOWN | 0.62 | 0.67 | 0.17 |
| 11-02 13:06 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 13:06 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 11-02 13:06 | +15 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 11-02 13:06 | +10 | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 13:06 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.48 |
| 11-02 13:05 | +10 stop | XRP | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 13:05 | +10 | XRP | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 13:05 | +5 | XRP | DOWN | 0.54 | 0.68 | 1.06 |
| 11-02 13:05 | +10 stop | SOL | UP | 0.52 | 0.20 | -3.50 |
| 11-02 13:05 | +10 stop | HYPE | DOWN | 0.66 | 0.79 | 0.98 |
| 11-02 13:05 | +15 | HYPE | DOWN | 0.67 | 0.83 | 1.30 |
| 11-02 13:05 | +10 | HYPE | DOWN | 0.67 | 0.79 | 0.88 |
| 11-02 13:05 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-02 13:05 | +10 stop | BNB | DOWN | 0.69 | 0.82 | 0.99 |
| 11-02 13:05 | +10 | BNB | DOWN | 0.68 | 0.82 | 1.13 |
| 11-02 13:05 | +5 | BNB | DOWN | 0.68 | 0.82 | 1.13 |
| 11-02 13:05 | +10 stop | XRP | UP | 0.42 | 0.57 | 1.14 |
| 11-02 13:05 | +10 | XRP | UP | 0.42 | 0.57 | 1.14 |
| 11-02 13:05 | +5 | XRP | UP | 0.42 | 0.57 | 1.14 |
| 11-02 13:05 | +10 stop | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 11-02 13:05 | +10 | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 11-02 13:04 | +10 stop | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-02 13:04 | +10 | DOGE | DOWN | 0.56 | 0.67 | 0.76 |
| 11-02 13:04 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
