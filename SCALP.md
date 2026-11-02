# Range-Scalp Bot

*Updated Mon Nov 02 08:00 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44639 | 38872 | 5767 (65) | 3 | $-12903.32 | -4.6% |
| **+10¢** | 33318 | 26645 | 6673 (86) | 7 | $-11707.71 | -5.6% |
| **+15¢** | 27884 | 20704 | 7180 (113) | 7 | $-10720.86 | -6.1% |
| **+20¢** | 24782 | 17266 | 7516 (147) | 7 | $-9427.22 | -6.1% |
| **+10¢ (15¢ stop)** | 54485 | 54399 | 86 (51) | 0 | $-20643.88 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 07:58 | +10 stop | HYPE | UP | 0.16 | 0.53 | 3.38 |
| 11-02 07:58 | +5 | HYPE | UP | 0.17 | 0.53 | 3.33 |
| 11-02 07:53 | +10 stop | HYPE | UP | 0.71 | 0.52 | -2.23 |
| 11-02 07:53 | +5 | HYPE | UP | 0.71 | 0.76 | 0.22 |
| 11-02 07:53 | +10 stop | HYPE | DOWN | 0.48 | 0.60 | 0.85 |
| 11-02 07:53 | +20 | HYPE | DOWN | 0.48 | 0.95 | 4.48 |
| 11-02 07:53 | +15 | HYPE | DOWN | 0.48 | 0.95 | 4.48 |
| 11-02 07:53 | +10 | HYPE | DOWN | 0.52 | 0.95 | 4.08 |
| 11-02 07:53 | +5 | HYPE | DOWN | 0.52 | 0.60 | 0.45 |
| 11-02 07:52 | +5 | BTC | DOWN | 0.51 | 0.59 | 0.45 |
| 11-02 07:50 | +5 | SOL | UP | 0.66 | 0.73 | 0.40 |
| 11-02 07:50 | +10 stop | XRP | UP | 0.64 | 0.81 | 1.42 |
| 11-02 07:49 | +10 stop | BNB | UP | 0.63 | 0.75 | 0.89 |
| 11-02 07:49 | +5 | BNB | UP | 0.63 | 0.70 | 0.38 |
| 11-02 07:49 | +10 stop | ETH | UP | 0.63 | 0.81 | 1.52 |
| 11-02 07:49 | +5 | ETH | UP | 0.63 | 0.71 | 0.48 |
| 11-02 07:49 | +10 stop | BTC | DOWN | 0.70 | 0.51 | -2.23 |
| 11-02 07:49 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-02 07:49 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-02 07:49 | +5 | BTC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-02 07:49 | +10 stop | ZEC | UP | 0.60 | 0.73 | 0.99 |
| 11-02 07:49 | +10 stop | NEAR | UP | 0.62 | 0.75 | 0.99 |
| 11-02 07:49 | +10 stop | SOL | UP | 0.59 | 0.70 | 0.77 |
| 11-02 07:49 | +5 | SOL | UP | 0.59 | 0.65 | 0.27 |
| 11-02 07:49 | +10 stop | BNB | DOWN | 0.54 | 0.37 | -2.05 |
| 11-02 07:49 | +10 | BNB | DOWN | 0.54 | open |  |
| 11-02 07:49 | +5 | BNB | DOWN | 0.54 | 0.62 | 0.45 |
| 11-02 07:49 | +10 stop | XRP | UP | 0.54 | 0.72 | 1.47 |
| 11-02 07:48 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 11-02 07:48 | +20 | DOGE | UP | 0.67 | 0.87 | 1.76 |
| 11-02 07:48 | +15 | DOGE | UP | 0.68 | 0.84 | 1.34 |
| 11-02 07:48 | +10 | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-02 07:48 | +5 | DOGE | UP | 0.68 | 0.77 | 0.61 |
| 11-02 07:48 | +10 stop | XRP | DOWN | 0.57 | 0.42 | -1.86 |
| 11-02 07:48 | +10 stop | ZEC | DOWN | 0.62 | 0.46 | -1.95 |
| 11-02 07:47 | +10 stop | SOL | UP | 0.56 | 0.69 | 0.97 |
| 11-02 07:47 | +10 stop | NEAR | DOWN | 0.60 | 0.45 | -1.85 |
| 11-02 07:47 | +20 | NEAR | DOWN | 0.60 | open |  |
| 11-02 07:47 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-02 07:47 | +10 | NEAR | DOWN | 0.59 | open |  |
