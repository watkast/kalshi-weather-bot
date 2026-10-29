# Range-Scalp Bot

*Updated Thu Oct 29 01:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38754 | 33820 | 4934 (49) | 1 | $-10874.78 | -4.5% |
| **+10¢** | 28905 | 23207 | 5698 (71) | 2 | $-9635.18 | -5.3% |
| **+15¢** | 24178 | 18056 | 6122 (97) | 3 | $-8591.44 | -5.7% |
| **+20¢** | 21450 | 15039 | 6411 (125) | 6 | $-7491.80 | -5.6% |
| **+10¢ (15¢ stop)** | 47390 | 47323 | 67 (35) | 1 | $-17975.34 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 01:05 | +10 | DOGE | DOWN | 0.71 | open |  |
| 10-29 01:05 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 10-29 01:05 | +5 | NEAR | DOWN | 0.68 | open |  |
| 10-29 01:02 | +10 stop | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 01:02 | +20 | NEAR | DOWN | 0.61 | open |  |
| 10-29 01:02 | +15 | NEAR | DOWN | 0.62 | open |  |
| 10-29 01:02 | +10 | NEAR | DOWN | 0.62 | open |  |
| 10-29 01:02 | +5 | NEAR | DOWN | 0.62 | 0.71 | 0.58 |
| 10-29 01:02 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-29 01:01 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-29 01:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-29 01:01 | +15 | BTC | DOWN | 0.65 | 0.81 | 1.33 |
| 10-29 01:01 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-29 01:01 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 10-29 01:01 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 01:01 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-29 01:01 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-29 01:01 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 01:01 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 01:01 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 01:01 | +20 | HYPE | DOWN | 0.61 | open |  |
| 10-29 01:01 | +15 | HYPE | DOWN | 0.61 | 0.76 | 1.20 |
| 10-29 01:01 | +10 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 01:01 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 10-29 01:01 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-29 01:01 | +20 | SOL | DOWN | 0.71 | open |  |
| 10-29 01:01 | +15 | SOL | DOWN | 0.71 | open |  |
| 10-29 01:01 | +10 | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-29 01:01 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-29 01:01 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 10-29 01:01 | +20 | XRP | DOWN | 0.69 | 0.89 | 1.78 |
| 10-29 01:01 | +15 | XRP | DOWN | 0.69 | 0.88 | 1.67 |
| 10-29 01:01 | +10 | XRP | DOWN | 0.69 | 0.88 | 1.67 |
| 10-29 01:01 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 10-29 01:01 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-29 01:01 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.85 |
| 10-29 01:01 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-29 01:01 | +10 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 10-29 01:01 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-29 01:01 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.81 |
