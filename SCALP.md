# Range-Scalp Bot

*Updated Mon Nov 23 01:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69403 | 60557 | 8846 (146) | 1 | $-18691.74 | -4.3% |
| **+10¢** | 51791 | 41456 | 10335 (189) | 1 | $-17387.99 | -5.3% |
| **+15¢** | 43401 | 32268 | 11133 (244) | 2 | $-15536.41 | -5.7% |
| **+20¢** | 38654 | 26950 | 11704 (306) | 2 | $-13828.84 | -5.7% |
| **+10¢ (15¢ stop)** | 84500 | 84310 | 190 (118) | 0 | $-31060.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 01:53 | +10 stop | ZEC | DOWN | 0.65 | 0.46 | -2.24 |
| 11-23 01:53 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 11-23 01:53 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-23 01:53 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-23 01:53 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-23 01:53 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-23 01:53 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-23 01:52 | +10 stop | HYPE | DOWN | 0.70 | 0.80 | 0.73 |
| 11-23 01:51 | +10 stop | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-23 01:51 | +20 | NEAR | UP | 0.61 | open |  |
| 11-23 01:51 | +15 | NEAR | UP | 0.61 | open |  |
| 11-23 01:51 | +10 | NEAR | UP | 0.61 | 0.71 | 0.68 |
| 11-23 01:51 | +5 | NEAR | UP | 0.61 | 0.70 | 0.58 |
| 11-23 01:47 | +10 stop | HYPE | DOWN | 0.66 | 0.49 | -2.04 |
| 11-23 01:47 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-23 01:47 | +15 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 11-23 01:47 | +10 | HYPE | DOWN | 0.66 | 0.76 | 0.71 |
| 11-23 01:47 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-23 01:46 | +20 | BNB | DOWN | 0.70 | 0.93 | 2.05 |
| 11-23 01:46 | +15 | BNB | DOWN | 0.70 | 0.85 | 1.26 |
| 11-23 01:46 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.84 |
| 11-23 01:46 | +5 | BNB | DOWN | 0.70 | 0.79 | 0.63 |
| 11-23 01:46 | +10 stop | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 01:46 | +20 | ETH | DOWN | 0.63 | 0.84 | 1.83 |
| 11-23 01:46 | +15 | ETH | DOWN | 0.63 | 0.81 | 1.52 |
| 11-23 01:46 | +10 | ETH | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 01:46 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.58 |
| 11-23 01:46 | +10 stop | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-23 01:46 | +20 | DOGE | DOWN | 0.58 | 0.80 | 1.90 |
| 11-23 01:46 | +15 | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
| 11-23 01:46 | +10 | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-23 01:46 | +5 | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-23 01:46 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-23 01:46 | +20 | SOL | DOWN | 0.61 | 0.85 | 2.14 |
| 11-23 01:46 | +15 | SOL | DOWN | 0.62 | 0.77 | 1.20 |
| 11-23 01:46 | +10 | SOL | DOWN | 0.62 | 0.73 | 0.79 |
| 11-23 01:46 | +5 | SOL | DOWN | 0.62 | 0.71 | 0.58 |
| 11-23 01:46 | +10 stop | XRP | DOWN | 0.63 | 0.74 | 0.79 |
| 11-23 01:46 | +20 | XRP | DOWN | 0.63 | 0.85 | 1.94 |
| 11-23 01:46 | +15 | XRP | DOWN | 0.63 | 0.78 | 1.20 |
