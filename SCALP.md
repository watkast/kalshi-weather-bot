# Range-Scalp Bot

*Updated Wed Nov 04 10:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47111 | 41024 | 6087 (72) | 2 | $-13566.69 | -4.6% |
| **+10¢** | 35200 | 28140 | 7060 (97) | 4 | $-12384.64 | -5.6% |
| **+15¢** | 29478 | 21876 | 7602 (125) | 4 | $-11360.04 | -6.1% |
| **+20¢** | 26188 | 18226 | 7962 (165) | 4 | $-10017.43 | -6.1% |
| **+10¢ (15¢ stop)** | 57419 | 57326 | 93 (56) | 4 | $-21392.47 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 10:46 | +10 stop | BNB | DOWN | 0.61 | open |  |
| 11-04 10:46 | +20 | BNB | DOWN | 0.61 | open |  |
| 11-04 10:46 | +15 | BNB | DOWN | 0.61 | open |  |
| 11-04 10:46 | +10 | BNB | DOWN | 0.61 | open |  |
| 11-04 10:46 | +5 | BNB | DOWN | 0.61 | open |  |
| 11-04 10:45 | +10 stop | NEAR | DOWN | 0.47 | open |  |
| 11-04 10:45 | +20 | NEAR | DOWN | 0.47 | open |  |
| 11-04 10:45 | +15 | NEAR | DOWN | 0.47 | open |  |
| 11-04 10:45 | +10 | NEAR | DOWN | 0.47 | open |  |
| 11-04 10:45 | +5 | NEAR | DOWN | 0.47 | 0.54 | 0.34 |
| 11-04 10:45 | +10 stop | DOGE | DOWN | 0.49 | open |  |
| 11-04 10:45 | +20 | DOGE | DOWN | 0.49 | open |  |
| 11-04 10:45 | +15 | DOGE | DOWN | 0.49 | open |  |
| 11-04 10:45 | +10 | DOGE | DOWN | 0.49 | open |  |
| 11-04 10:45 | +5 | DOGE | DOWN | 0.49 | 0.54 | 0.14 |
| 11-04 10:45 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 11-04 10:45 | +20 | ZEC | DOWN | 0.64 | open |  |
| 11-04 10:45 | +15 | ZEC | DOWN | 0.64 | open |  |
| 11-04 10:45 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-04 10:45 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-04 10:43 | +10 stop | ZEC | DOWN | 0.70 | 0.91 | 1.89 |
| 11-04 10:41 | +10 stop | ZEC | UP | 0.67 | 0.34 | -3.62 |
| 11-04 10:40 | +10 stop | ZEC | DOWN | 0.65 | 0.32 | -3.62 |
| 11-04 10:40 | +10 | ZEC | DOWN | 0.67 | 0.77 | 0.71 |
| 11-04 10:40 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-04 10:38 | +10 stop | HYPE | DOWN | 0.53 | 0.86 | 3.03 |
| 11-04 10:37 | +10 stop | ZEC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-04 10:37 | +10 stop | NEAR | DOWN | 0.71 | 0.56 | -1.83 |
| 11-04 10:37 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.84 |
| 11-04 10:37 | +15 | NEAR | DOWN | 0.71 | 0.90 | 1.68 |
| 11-04 10:37 | +10 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 10:37 | +5 | NEAR | DOWN | 0.71 | 0.82 | 0.84 |
| 11-04 10:37 | +10 stop | HYPE | UP | 0.55 | 0.38 | -2.05 |
| 11-04 10:37 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-04 10:36 | +10 stop | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 11-04 10:36 | +10 stop | ZEC | UP | 0.64 | 0.44 | -2.35 |
| 11-04 10:35 | +10 stop | ETH | UP | 0.58 | 0.37 | -2.45 |
| 11-04 10:35 | +10 | ETH | UP | 0.58 | no | -5.98 |
| 11-04 10:35 | +5 | ETH | UP | 0.58 | no | -5.98 |
| 11-04 10:34 | +10 stop | BNB | UP | 0.71 | 0.50 | -2.43 |
