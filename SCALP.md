# Range-Scalp Bot

*Updated Mon Oct 19 01:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23314 | 20273 | 3041 (30) | 1 | $-6946.84 | -4.7% |
| **+10¢** | 17537 | 14031 | 3506 (44) | 1 | $-6193.41 | -5.6% |
| **+15¢** | 14696 | 10917 | 3779 (66) | 2 | $-5631.40 | -6.1% |
| **+20¢** | 13009 | 9056 | 3953 (84) | 2 | $-5014.16 | -6.1% |
| **+10¢ (15¢ stop)** | 28703 | 28652 | 51 (30) | 1 | $-10937.92 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 01:57 | +10 stop | BNB | UP | 0.59 | open |  |
| 10-19 01:56 | +10 stop | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 10-19 01:56 | +10 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 10-19 01:56 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-19 01:55 | +10 stop | BNB | UP | 0.63 | 0.79 | 1.31 |
| 10-19 01:54 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-19 01:54 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.90 |
| 10-19 01:54 | +10 stop | DOGE | UP | 0.39 | 0.60 | 1.76 |
| 10-19 01:53 | +10 stop | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-19 01:53 | +20 | ETH | DOWN | 0.68 | 0.88 | 1.76 |
| 10-19 01:53 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-19 01:53 | +10 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-19 01:53 | +5 | ETH | DOWN | 0.68 | 0.74 | 0.30 |
| 10-19 01:53 | +10 stop | SOL | UP | 0.60 | 0.35 | -2.83 |
| 10-19 01:53 | +10 stop | ZEC | UP | 0.63 | 0.41 | -2.54 |
| 10-19 01:52 | +10 stop | BNB | UP | 0.59 | 0.70 | 0.78 |
| 10-19 01:52 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-19 01:52 | +10 stop | DOGE | DOWN | 0.61 | 0.38 | -2.64 |
| 10-19 01:52 | +5 | SOL | DOWN | 0.53 | 0.64 | 0.75 |
| 10-19 01:52 | +10 stop | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 10-19 01:52 | +10 | XRP | DOWN | 0.63 | 0.75 | 0.89 |
| 10-19 01:51 | +5 | SOL | DOWN | 0.54 | 0.62 | 0.45 |
| 10-19 01:51 | +5 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 10-19 01:51 | +10 stop | HYPE | DOWN | 0.62 | 0.42 | -2.35 |
| 10-19 01:51 | +10 | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
| 10-19 01:51 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-19 01:50 | +10 stop | SOL | DOWN | 0.63 | 0.46 | -2.05 |
| 10-19 01:50 | +20 | SOL | DOWN | 0.63 | 0.95 | 3.01 |
| 10-19 01:50 | +15 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 10-19 01:50 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-19 01:50 | +5 | SOL | DOWN | 0.62 | 0.70 | 0.48 |
| 10-19 01:50 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 10-19 01:50 | +20 | DOGE | DOWN | 0.69 | 0.90 | 1.91 |
| 10-19 01:50 | +15 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-19 01:50 | +10 | DOGE | DOWN | 0.69 | 0.85 | 1.36 |
| 10-19 01:50 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-19 01:50 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.01 |
| 10-19 01:50 | +10 | BNB | DOWN | 0.59 | open |  |
| 10-19 01:50 | +5 | BNB | DOWN | 0.59 | open |  |
| 10-19 01:50 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
