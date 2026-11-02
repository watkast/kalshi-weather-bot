# Range-Scalp Bot

*Updated Mon Nov 02 21:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45183 | 39345 | 5838 (67) | 4 | $-13055.97 | -4.6% |
| **+10¢** | 33722 | 26957 | 6765 (88) | 4 | $-11933.18 | -5.6% |
| **+15¢** | 28204 | 20925 | 7279 (115) | 5 | $-10979.27 | -6.2% |
| **+20¢** | 25046 | 17424 | 7622 (150) | 5 | $-9733.79 | -6.2% |
| **+10¢ (15¢ stop)** | 55114 | 55027 | 87 (51) | 3 | $-20826.31 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 21:53 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-02 21:52 | +10 stop | SOL | DOWN | 0.59 | open |  |
| 11-02 21:52 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-02 21:51 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-02 21:51 | +5 | BNB | DOWN | 0.65 | open |  |
| 11-02 21:48 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.19 |
| 11-02 21:48 | +5 | SOL | DOWN | 0.57 | 0.65 | 0.46 |
| 11-02 21:48 | +10 stop | BNB | DOWN | 0.61 | 0.75 | 1.09 |
| 11-02 21:48 | +10 stop | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-02 21:48 | +5 | NEAR | DOWN | 0.56 | 0.63 | 0.35 |
| 11-02 21:48 | +5 | BNB | DOWN | 0.57 | 0.63 | 0.25 |
| 11-02 21:48 | +5 | DOGE | UP | 0.61 | open |  |
| 11-02 21:47 | +10 stop | DOGE | UP | 0.60 | open |  |
| 11-02 21:47 | +10 | DOGE | UP | 0.60 | open |  |
| 11-02 21:47 | +5 | DOGE | UP | 0.60 | 0.65 | 0.17 |
| 11-02 21:47 | +5 | BNB | UP | 0.52 | 0.60 | 0.45 |
| 11-02 21:47 | +10 stop | HYPE | UP | 0.71 | 0.82 | 0.86 |
| 11-02 21:47 | +20 | HYPE | UP | 0.71 | open |  |
| 11-02 21:47 | +15 | HYPE | UP | 0.71 | open |  |
| 11-02 21:47 | +10 | HYPE | UP | 0.71 | 0.82 | 0.86 |
| 11-02 21:47 | +5 | HYPE | UP | 0.71 | 0.82 | 0.87 |
| 11-02 21:47 | +10 stop | BNB | UP | 0.60 | 0.34 | -2.93 |
| 11-02 21:47 | +20 | BNB | UP | 0.60 | open |  |
| 11-02 21:47 | +15 | BNB | UP | 0.60 | open |  |
| 11-02 21:47 | +10 | BNB | UP | 0.60 | open |  |
| 11-02 21:47 | +5 | BNB | UP | 0.60 | 0.66 | 0.27 |
| 11-02 21:46 | +10 stop | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-02 21:46 | +20 | BTC | DOWN | 0.68 | 0.91 | 2.11 |
| 11-02 21:46 | +15 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-02 21:46 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-02 21:46 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-02 21:46 | +10 stop | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-02 21:46 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-02 21:46 | +15 | ZEC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-02 21:46 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-02 21:46 | +5 | ZEC | DOWN | 0.64 | 0.71 | 0.38 |
| 11-02 21:46 | +10 stop | XRP | UP | 0.62 | 0.37 | -2.84 |
| 11-02 21:46 | +20 | XRP | UP | 0.62 | open |  |
| 11-02 21:46 | +15 | XRP | UP | 0.62 | open |  |
| 11-02 21:46 | +10 | XRP | UP | 0.62 | open |  |
