# Range-Scalp Bot

*Updated Tue Nov 10 14:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54630 | 47655 | 6975 (91) | 1 | $-14866.05 | -4.3% |
| **+10¢** | 40817 | 32675 | 8142 (121) | 0 | $-13810.21 | -5.4% |
| **+15¢** | 34218 | 25440 | 8778 (155) | 2 | $-12566.74 | -5.9% |
| **+20¢** | 30467 | 21258 | 9209 (204) | 3 | $-10981.26 | -5.7% |
| **+10¢ (15¢ stop)** | 66551 | 66437 | 114 (70) | 0 | $-24589.96 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 14:53 | +5 | BNB | DOWN | 0.70 | open |  |
| 11-10 14:52 | +10 stop | BNB | DOWN | 0.60 | 0.70 | 0.69 |
| 11-10 14:52 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-10 14:52 | +10 | BNB | DOWN | 0.60 | 0.70 | 0.69 |
| 11-10 14:52 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.48 |
| 11-10 14:52 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.81 |
| 11-10 14:52 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-10 14:52 | +15 | ZEC | DOWN | 0.70 | open |  |
| 11-10 14:52 | +10 | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-10 14:52 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-10 14:52 | +10 stop | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-10 14:52 | +15 | HYPE | DOWN | 0.56 | 0.74 | 1.48 |
| 11-10 14:52 | +10 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-10 14:52 | +5 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 11-10 14:47 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-10 14:46 | +5 | BNB | DOWN | 0.66 | 0.75 | 0.61 |
| 11-10 14:46 | +10 stop | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 11-10 14:46 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-10 14:46 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 11-10 14:46 | +10 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 11-10 14:46 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-10 14:46 | +10 stop | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-10 14:46 | +20 | BTC | DOWN | 0.63 | 0.85 | 1.94 |
| 11-10 14:46 | +15 | BTC | DOWN | 0.63 | 0.78 | 1.20 |
| 11-10 14:46 | +10 | BTC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-10 14:46 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-10 14:46 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 14:46 | +20 | DOGE | DOWN | 0.66 | 0.91 | 2.28 |
| 11-10 14:46 | +15 | DOGE | DOWN | 0.66 | 0.81 | 1.23 |
| 11-10 14:46 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 14:46 | +5 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-10 14:46 | +10 stop | HYPE | DOWN | 0.68 | 0.87 | 1.66 |
| 11-10 14:46 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-10 14:46 | +15 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-10 14:46 | +10 | HYPE | DOWN | 0.68 | 0.87 | 1.66 |
| 11-10 14:46 | +5 | HYPE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-10 14:46 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 14:46 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-10 14:46 | +15 | BNB | DOWN | 0.65 | 0.84 | 1.64 |
| 11-10 14:46 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
