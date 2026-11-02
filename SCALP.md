# Range-Scalp Bot

*Updated Mon Nov 02 23:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 45280 | 39432 | 5848 (67) | 2 | $-13050.06 | -4.6% |
| **+10¢** | 33792 | 27016 | 6776 (88) | 3 | $-11928.41 | -5.6% |
| **+15¢** | 28266 | 20974 | 7292 (115) | 3 | $-10977.21 | -6.2% |
| **+20¢** | 25103 | 17466 | 7637 (150) | 3 | $-9735.42 | -6.2% |
| **+10¢ (15¢ stop)** | 55228 | 55141 | 87 (51) | 0 | $-20834.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-02 23:14 | +10 stop | NEAR | UP | 0.20 | 0.68 | 4.52 |
| 11-02 23:14 | +5 | NEAR | UP | 0.29 | 0.68 | 3.59 |
| 11-02 23:12 | +10 stop | ETH | DOWN | 0.67 | 0.94 | 2.47 |
| 11-02 23:11 | +10 stop | ZEC | DOWN | 0.64 | 0.93 | 2.69 |
| 11-02 23:11 | +20 | ZEC | DOWN | 0.64 | 0.93 | 2.69 |
| 11-02 23:11 | +15 | ZEC | DOWN | 0.64 | 0.93 | 2.69 |
| 11-02 23:11 | +10 | ZEC | DOWN | 0.64 | 0.93 | 2.69 |
| 11-02 23:11 | +5 | ZEC | DOWN | 0.64 | 0.72 | 0.48 |
| 11-02 23:11 | +10 | ETH | DOWN | 0.62 | 0.94 | 2.96 |
| 11-02 23:11 | +5 | ETH | DOWN | 0.63 | 0.94 | 2.87 |
| 11-02 23:11 | +10 stop | SOL | UP | 0.67 | 0.80 | 1.02 |
| 11-02 23:11 | +5 | SOL | UP | 0.68 | 0.75 | 0.40 |
| 11-02 23:10 | +10 stop | ETH | DOWN | 0.70 | 0.49 | -2.43 |
| 11-02 23:10 | +20 | ETH | DOWN | 0.68 | 0.94 | 2.37 |
| 11-02 23:10 | +15 | ETH | DOWN | 0.68 | 0.94 | 2.37 |
| 11-02 23:10 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 23:10 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-02 23:09 | +10 stop | BNB | DOWN | 0.70 | 0.50 | -2.35 |
| 11-02 23:09 | +20 | BNB | DOWN | 0.70 | 0.97 | 2.52 |
| 11-02 23:09 | +15 | BNB | DOWN | 0.70 | 0.97 | 2.52 |
| 11-02 23:09 | +10 | BNB | DOWN | 0.70 | 0.97 | 2.52 |
| 11-02 23:09 | +5 | BNB | DOWN | 0.70 | 0.97 | 2.52 |
| 11-02 23:09 | +10 stop | SOL | DOWN | 0.56 | 0.40 | -1.95 |
| 11-02 23:09 | +20 | SOL | DOWN | 0.56 | 0.79 | 2.00 |
| 11-02 23:09 | +15 | SOL | DOWN | 0.56 | 0.79 | 2.00 |
| 11-02 23:09 | +10 | SOL | DOWN | 0.56 | 0.79 | 2.00 |
| 11-02 23:09 | +5 | SOL | DOWN | 0.56 | 0.61 | 0.15 |
| 11-02 23:09 | +10 stop | NEAR | DOWN | 0.29 | 0.57 | 2.47 |
| 11-02 23:09 | +5 | NEAR | DOWN | 0.40 | 0.57 | 1.35 |
| 11-02 23:07 | +5 | HYPE | DOWN | 0.69 | open |  |
| 11-02 23:07 | +10 stop | DOGE | UP | 0.64 | 0.87 | 2.05 |
| 11-02 23:07 | +10 | DOGE | UP | 0.64 | 0.87 | 2.05 |
| 11-02 23:07 | +5 | DOGE | UP | 0.64 | 0.87 | 2.05 |
| 11-02 23:07 | +10 stop | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 11-02 23:07 | +20 | DOGE | UP | 0.55 | 0.87 | 2.94 |
| 11-02 23:07 | +15 | DOGE | UP | 0.55 | 0.87 | 2.94 |
| 11-02 23:07 | +10 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 11-02 23:07 | +5 | DOGE | UP | 0.55 | 0.68 | 0.96 |
| 11-02 23:07 | +5 | NEAR | UP | 0.47 | 0.57 | 0.64 |
| 11-02 23:07 | +10 stop | HYPE | DOWN | 0.57 | 0.41 | -1.96 |
