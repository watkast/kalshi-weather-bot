# Range-Scalp Bot

*Updated Tue Nov 24 06:44 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70542 | 61578 | 8964 (148) | 3 | $-18815.13 | -4.2% |
| **+10¢** | 52629 | 42164 | 10465 (192) | 4 | $-17401.21 | -5.3% |
| **+15¢** | 44086 | 32815 | 11271 (248) | 5 | $-15464.61 | -5.6% |
| **+20¢** | 39259 | 27393 | 11866 (314) | 5 | $-13822.03 | -5.6% |
| **+10¢ (15¢ stop)** | 85896 | 85698 | 198 (118) | 0 | $-31570.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 06:43 | +10 stop | BTC | UP | 0.61 | 0.73 | 0.89 |
| 11-24 06:43 | +5 | BTC | UP | 0.64 | 0.73 | 0.59 |
| 11-24 06:41 | +10 stop | ZEC | DOWN | 0.70 | 0.81 | 0.80 |
| 11-24 06:41 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-24 06:41 | +10 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 06:41 | +5 | ZEC | DOWN | 0.70 | 0.81 | 0.84 |
| 11-24 06:41 | +10 | NEAR | UP | 0.65 | open |  |
| 11-24 06:41 | +5 | NEAR | UP | 0.65 | 0.72 | 0.39 |
| 11-24 06:41 | +10 stop | NEAR | UP | 0.66 | 0.46 | -2.34 |
| 11-24 06:41 | +10 stop | ETH | UP | 0.69 | 0.80 | 0.83 |
| 11-24 06:39 | +10 stop | ETH | DOWN | 0.60 | 0.40 | -2.34 |
| 11-24 06:39 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-24 06:39 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-24 06:39 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-24 06:39 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-24 06:38 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-24 06:38 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-24 06:38 | +10 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 06:38 | +5 | HYPE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-24 06:38 | +10 stop | DOGE | DOWN | 0.63 | 0.48 | -1.85 |
| 11-24 06:37 | +10 stop | BNB | DOWN | 0.64 | 0.46 | -2.15 |
| 11-24 06:37 | +20 | BNB | DOWN | 0.64 | open |  |
| 11-24 06:37 | +15 | BNB | DOWN | 0.64 | open |  |
| 11-24 06:37 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-24 06:37 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-24 06:37 | +10 stop | NEAR | UP | 0.63 | 0.48 | -1.87 |
| 11-24 06:37 | +20 | NEAR | UP | 0.63 | open |  |
| 11-24 06:37 | +15 | NEAR | UP | 0.63 | open |  |
| 11-24 06:37 | +10 | NEAR | UP | 0.63 | 0.75 | 0.89 |
| 11-24 06:37 | +5 | NEAR | UP | 0.63 | 0.71 | 0.48 |
| 11-24 06:36 | +10 stop | BTC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-24 06:36 | +10 stop | ZEC | DOWN | 0.61 | 0.78 | 1.40 |
| 11-24 06:36 | +10 stop | HYPE | DOWN | 0.68 | 0.52 | -1.94 |
| 11-24 06:36 | +10 stop | SOL | UP | 0.70 | 0.87 | 1.47 |
| 11-24 06:36 | +15 | SOL | UP | 0.70 | 0.87 | 1.47 |
| 11-24 06:36 | +10 | SOL | UP | 0.70 | 0.87 | 1.47 |
| 11-24 06:36 | +5 | SOL | UP | 0.70 | 0.75 | 0.21 |
| 11-24 06:35 | +10 stop | XRP | UP | 0.38 | 0.55 | 1.35 |
| 11-24 06:35 | +10 stop | DOGE | UP | 0.43 | 0.61 | 1.45 |
| 11-24 06:35 | +10 stop | HYPE | UP | 0.44 | 0.55 | 0.74 |
