# Range-Scalp Bot

*Updated Mon Nov 02 11:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 44796 | 39010 | 5786 (65) | 2 | $-12938.86 | -4.6% |
| **+10¢** | 33439 | 26738 | 6701 (86) | 2 | $-11782.17 | -5.6% |
| **+15¢** | 27975 | 20763 | 7212 (113) | 2 | $-10826.08 | -6.2% |
| **+20¢** | 24855 | 17306 | 7549 (148) | 2 | $-9540.07 | -6.1% |
| **+10¢ (15¢ stop)** | 54676 | 54589 | 87 (51) | 0 | $-20681.29 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 11:39 | +10 stop | BTC | UP | 0.69 | 0.94 | 2.26 |
| 11-02 11:39 | +15 | BTC | UP | 0.69 | 0.94 | 2.26 |
| 11-02 11:39 | +10 | BTC | UP | 0.69 | 0.94 | 2.26 |
| 11-02 11:39 | +5 | BTC | UP | 0.69 | 0.75 | 0.31 |
| 11-02 11:39 | +10 stop | SOL | UP | 0.62 | 0.85 | 2.04 |
| 11-02 11:39 | +15 | SOL | UP | 0.62 | 0.85 | 2.04 |
| 11-02 11:39 | +10 | SOL | UP | 0.62 | 0.85 | 2.04 |
| 11-02 11:39 | +5 | SOL | UP | 0.62 | 0.68 | 0.27 |
| 11-02 11:39 | +10 stop | ETH | UP | 0.64 | 0.91 | 2.51 |
| 11-02 11:39 | +20 | ETH | UP | 0.64 | 0.91 | 2.51 |
| 11-02 11:39 | +15 | ETH | UP | 0.64 | 0.91 | 2.51 |
| 11-02 11:39 | +10 | ETH | UP | 0.64 | 0.91 | 2.51 |
| 11-02 11:39 | +5 | ETH | UP | 0.64 | 0.70 | 0.28 |
| 11-02 11:38 | +10 stop | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-02 11:38 | +10 | XRP | DOWN | 0.58 | 0.71 | 0.97 |
| 11-02 11:38 | +5 | XRP | DOWN | 0.57 | 0.71 | 1.07 |
| 11-02 11:36 | +10 stop | BTC | UP | 0.71 | 0.84 | 1.05 |
| 11-02 11:34 | +10 stop | SOL | UP | 0.61 | 0.77 | 1.30 |
| 11-02 11:34 | +10 stop | HYPE | UP | 0.67 | 0.79 | 0.95 |
| 11-02 11:34 | +10 stop | DOGE | UP | 0.62 | 0.78 | 1.30 |
| 11-02 11:34 | +10 stop | DOGE | DOWN | 0.37 | 0.53 | 1.25 |
| 11-02 11:33 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-02 11:33 | +10 stop | BNB | DOWN | 0.55 | 0.37 | -2.15 |
| 11-02 11:33 | +10 | BNB | DOWN | 0.55 | open |  |
| 11-02 11:33 | +10 stop | ETH | DOWN | 0.58 | 0.41 | -2.05 |
| 11-02 11:33 | +10 stop | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 11-02 11:33 | +20 | NEAR | UP | 0.67 | 0.87 | 1.76 |
| 11-02 11:33 | +15 | NEAR | UP | 0.67 | 0.87 | 1.76 |
| 11-02 11:33 | +10 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-02 11:33 | +5 | NEAR | UP | 0.67 | 0.81 | 1.13 |
| 11-02 11:33 | +10 stop | HYPE | DOWN | 0.64 | 0.36 | -3.14 |
| 11-02 11:33 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-02 11:33 | +15 | HYPE | DOWN | 0.64 | open |  |
| 11-02 11:33 | +10 | HYPE | DOWN | 0.64 | open |  |
| 11-02 11:33 | +5 | HYPE | DOWN | 0.65 | open |  |
| 11-02 11:33 | +10 stop | SOL | UP | 0.53 | 0.64 | 0.75 |
| 11-02 11:33 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-02 11:33 | +10 stop | ZEC | UP | 0.62 | 0.76 | 1.10 |
| 11-02 11:33 | +10 | ZEC | UP | 0.62 | 0.76 | 1.10 |
| 11-02 11:33 | +5 | ZEC | UP | 0.62 | 0.71 | 0.58 |
