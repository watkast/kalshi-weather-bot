# Range-Scalp Bot

*Updated Mon Nov 16 12:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62086 | 54172 | 7914 (115) | 2 | $-16761.37 | -4.3% |
| **+10¢** | 46365 | 37104 | 9261 (157) | 2 | $-15630.43 | -5.4% |
| **+15¢** | 38849 | 28859 | 9990 (196) | 1 | $-14245.12 | -5.8% |
| **+20¢** | 34633 | 24160 | 10473 (249) | 1 | $-12410.13 | -5.7% |
| **+10¢ (15¢ stop)** | 75566 | 75412 | 154 (90) | 0 | $-27883.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 12:34 | +10 stop | ZEC | UP | 0.65 | 0.22 | -4.59 |
| 11-16 12:34 | +10 | ZEC | UP | 0.65 | open |  |
| 11-16 12:34 | +5 | ZEC | UP | 0.65 | open |  |
| 11-16 12:33 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-16 12:33 | +10 | SOL | UP | 0.70 | 0.82 | 0.94 |
| 11-16 12:33 | +5 | SOL | UP | 0.70 | 0.77 | 0.42 |
| 11-16 12:33 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 11-16 12:32 | +10 stop | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-16 12:32 | +20 | BNB | UP | 0.66 | 0.86 | 1.75 |
| 11-16 12:32 | +15 | BNB | UP | 0.66 | 0.81 | 1.23 |
| 11-16 12:32 | +10 | BNB | UP | 0.66 | 0.77 | 0.81 |
| 11-16 12:32 | +5 | BNB | UP | 0.65 | 0.71 | 0.29 |
| 11-16 12:32 | +10 stop | ZEC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-16 12:32 | +20 | ZEC | DOWN | 0.56 | 0.77 | 1.79 |
| 11-16 12:32 | +15 | ZEC | DOWN | 0.56 | 0.77 | 1.79 |
| 11-16 12:32 | +10 | ZEC | DOWN | 0.55 | 0.67 | 0.86 |
| 11-16 12:32 | +5 | ZEC | DOWN | 0.56 | 0.67 | 0.76 |
| 11-16 12:31 | +10 stop | HYPE | DOWN | 0.53 | 0.38 | -1.85 |
| 11-16 12:31 | +20 | HYPE | DOWN | 0.53 | open |  |
| 11-16 12:31 | +15 | HYPE | DOWN | 0.53 | open |  |
| 11-16 12:31 | +10 | HYPE | DOWN | 0.53 | open |  |
| 11-16 12:31 | +5 | HYPE | DOWN | 0.53 | open |  |
| 11-16 12:31 | +10 stop | SOL | UP | 0.61 | 0.73 | 0.89 |
| 11-16 12:31 | +20 | SOL | UP | 0.60 | 0.82 | 1.92 |
| 11-16 12:31 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-16 12:31 | +10 | SOL | UP | 0.60 | 0.73 | 0.99 |
| 11-16 12:31 | +5 | SOL | UP | 0.60 | 0.69 | 0.58 |
| 11-16 12:31 | +10 stop | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-16 12:31 | +20 | DOGE | UP | 0.68 | 0.91 | 2.05 |
| 11-16 12:31 | +15 | DOGE | UP | 0.68 | 0.86 | 1.55 |
| 11-16 12:31 | +10 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-16 12:31 | +5 | DOGE | UP | 0.68 | 0.78 | 0.71 |
| 11-16 12:31 | +10 stop | XRP | UP | 0.67 | 0.80 | 1.02 |
| 11-16 12:31 | +20 | XRP | UP | 0.63 | 0.85 | 1.94 |
| 11-16 12:31 | +15 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 11-16 12:31 | +10 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 11-16 12:31 | +5 | XRP | UP | 0.65 | 0.73 | 0.50 |
| 11-16 12:31 | +10 stop | ETH | UP | 0.71 | 0.81 | 0.74 |
| 11-16 12:31 | +5 | ETH | UP | 0.71 | 0.79 | 0.53 |
| 11-16 12:31 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
