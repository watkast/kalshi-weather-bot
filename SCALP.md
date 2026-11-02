# Range-Scalp Bot

*Updated Mon Nov 02 22:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45228 | 39386 | 5842 (67) | 2 | $-13055.46 | -4.6% |
| **+10¢** | 33753 | 26983 | 6770 (88) | 4 | $-11938.39 | -5.6% |
| **+15¢** | 28231 | 20945 | 7286 (115) | 5 | $-10994.78 | -6.2% |
| **+20¢** | 25069 | 17438 | 7631 (150) | 5 | $-9759.63 | -6.2% |
| **+10¢ (15¢ stop)** | 55166 | 55079 | 87 (51) | 3 | $-20844.00 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 22:23 | +5 | HYPE | DOWN | 0.62 | 0.70 | 0.48 |
| 11-02 22:23 | +10 stop | DOGE | DOWN | 0.56 | open |  |
| 11-02 22:23 | +20 | DOGE | DOWN | 0.56 | open |  |
| 11-02 22:23 | +15 | DOGE | DOWN | 0.56 | open |  |
| 11-02 22:23 | +10 | DOGE | DOWN | 0.56 | open |  |
| 11-02 22:23 | +5 | DOGE | DOWN | 0.56 | 0.63 | 0.35 |
| 11-02 22:22 | +10 stop | HYPE | DOWN | 0.57 | 0.70 | 0.93 |
| 11-02 22:22 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 11-02 22:22 | +10 stop | ETH | UP | 0.67 | open |  |
| 11-02 22:22 | +20 | ETH | UP | 0.67 | open |  |
| 11-02 22:22 | +15 | ETH | UP | 0.67 | open |  |
| 11-02 22:22 | +10 | ETH | UP | 0.67 | open |  |
| 11-02 22:22 | +5 | ETH | UP | 0.67 | 0.72 | 0.19 |
| 11-02 22:21 | +10 stop | BNB | UP | 0.70 | 0.50 | -2.33 |
| 11-02 22:21 | +20 | BNB | UP | 0.70 | open |  |
| 11-02 22:21 | +15 | BNB | UP | 0.70 | open |  |
| 11-02 22:21 | +10 | BNB | UP | 0.70 | open |  |
| 11-02 22:21 | +5 | BNB | UP | 0.70 | open |  |
| 11-02 22:18 | +10 stop | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-02 22:18 | +15 | ZEC | UP | 0.68 | 0.85 | 1.45 |
| 11-02 22:18 | +10 | ZEC | UP | 0.68 | 0.82 | 1.13 |
| 11-02 22:18 | +5 | ZEC | UP | 0.70 | 0.76 | 0.32 |
| 11-02 22:18 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-02 22:17 | +10 stop | NEAR | UP | 0.59 | 0.44 | -1.85 |
| 11-02 22:16 | +10 stop | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-02 22:16 | +20 | BTC | UP | 0.60 | 0.91 | 2.86 |
| 11-02 22:16 | +15 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-02 22:16 | +10 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-02 22:16 | +5 | BTC | UP | 0.59 | 0.75 | 1.29 |
| 11-02 22:16 | +10 stop | SOL | UP | 0.66 | 0.78 | 0.91 |
| 11-02 22:16 | +20 | SOL | UP | 0.66 | 0.86 | 1.75 |
| 11-02 22:16 | +15 | SOL | UP | 0.66 | 0.85 | 1.65 |
| 11-02 22:16 | +10 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 11-02 22:16 | +5 | SOL | UP | 0.66 | 0.78 | 0.91 |
| 11-02 22:16 | +10 stop | DOGE | UP | 0.59 | 0.73 | 1.09 |
| 11-02 22:16 | +20 | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 11-02 22:16 | +15 | DOGE | UP | 0.58 | 0.73 | 1.18 |
| 11-02 22:16 | +10 | DOGE | UP | 0.58 | 0.73 | 1.18 |
| 11-02 22:16 | +5 | DOGE | UP | 0.58 | 0.73 | 1.18 |
| 11-02 22:16 | +10 stop | XRP | UP | 0.61 | 0.74 | 0.99 |
