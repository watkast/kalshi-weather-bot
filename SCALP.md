# Range-Scalp Bot

*Updated Wed Nov 04 01:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46631 | 40609 | 6022 (72) | 6 | $-13384.82 | -4.6% |
| **+10¢** | 34827 | 27848 | 6979 (96) | 7 | $-12196.39 | -5.6% |
| **+15¢** | 29164 | 21655 | 7509 (124) | 7 | $-11151.61 | -6.1% |
| **+20¢** | 25907 | 18041 | 7866 (164) | 7 | $-9820.80 | -6.0% |
| **+10¢ (15¢ stop)** | 56862 | 56769 | 93 (56) | 0 | $-21257.24 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 01:54 | +10 stop | BNB | UP | 0.70 | 0.82 | 0.94 |
| 11-04 01:52 | +10 stop | SOL | UP | 0.68 | 0.84 | 1.31 |
| 11-04 01:52 | +10 stop | BNB | DOWN | 0.54 | 0.34 | -2.30 |
| 11-04 01:51 | +10 stop | BTC | UP | 0.65 | 0.79 | 1.12 |
| 11-04 01:50 | +10 stop | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-04 01:50 | +20 | DOGE | UP | 0.58 | 0.83 | 2.22 |
| 11-04 01:50 | +15 | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 11-04 01:50 | +10 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-04 01:50 | +5 | DOGE | UP | 0.58 | 0.69 | 0.77 |
| 11-04 01:50 | +5 | ETH | UP | 0.66 | 0.77 | 0.81 |
| 11-04 01:50 | +10 stop | BNB | DOWN | 0.68 | 0.46 | -2.54 |
| 11-04 01:50 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-04 01:50 | +5 | BNB | DOWN | 0.68 | open |  |
| 11-04 01:50 | +10 stop | SOL | UP | 0.57 | 0.79 | 1.90 |
| 11-04 01:49 | +5 | ETH | UP | 0.60 | 0.71 | 0.78 |
| 11-04 01:48 | +10 stop | BTC | UP | 0.59 | 0.44 | -1.85 |
| 11-04 01:48 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-04 01:48 | +10 stop | SOL | UP | 0.64 | 0.49 | -1.85 |
| 11-04 01:48 | +10 stop | HYPE | UP | 0.69 | 0.79 | 0.73 |
| 11-04 01:48 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-04 01:48 | +10 stop | NEAR | UP | 0.64 | 0.74 | 0.69 |
| 11-04 01:47 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 11-04 01:47 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.89 |
| 11-04 01:47 | +20 | BNB | DOWN | 0.62 | open |  |
| 11-04 01:47 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-04 01:47 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.76 |
| 11-04 01:47 | +5 | BNB | DOWN | 0.62 | 0.73 | 0.76 |
| 11-04 01:47 | +10 stop | ETH | UP | 0.66 | 0.77 | 0.81 |
| 11-04 01:47 | +20 | ETH | UP | 0.66 | 0.87 | 1.86 |
| 11-04 01:47 | +15 | ETH | UP | 0.65 | 0.82 | 1.43 |
| 11-04 01:47 | +10 | ETH | UP | 0.65 | 0.77 | 0.91 |
| 11-04 01:47 | +5 | ETH | UP | 0.65 | 0.71 | 0.29 |
| 11-04 01:46 | +10 stop | XRP | DOWN | 0.53 | 0.37 | -1.95 |
| 11-04 01:46 | +20 | XRP | DOWN | 0.53 | open |  |
| 11-04 01:46 | +15 | XRP | DOWN | 0.53 | open |  |
| 11-04 01:46 | +10 | XRP | DOWN | 0.53 | open |  |
| 11-04 01:46 | +5 | XRP | DOWN | 0.53 | open |  |
| 11-04 01:46 | +10 stop | SOL | DOWN | 0.60 | 0.45 | -1.89 |
| 11-04 01:46 | +20 | SOL | DOWN | 0.60 | open |  |
| 11-04 01:46 | +15 | SOL | DOWN | 0.60 | open |  |
