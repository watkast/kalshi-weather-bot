# Range-Scalp Bot

*Updated Tue Nov 10 06:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54293 | 47356 | 6937 (89) | 4 | $-14823.52 | -4.3% |
| **+10¢** | 40567 | 32476 | 8091 (117) | 7 | $-13755.52 | -5.4% |
| **+15¢** | 34000 | 25277 | 8723 (150) | 7 | $-12523.99 | -5.9% |
| **+20¢** | 30279 | 21128 | 9151 (198) | 6 | $-10930.43 | -5.8% |
| **+10¢ (15¢ stop)** | 66149 | 66039 | 110 (66) | 5 | $-24448.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 06:34 | +10 stop | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 11-10 06:34 | +5 | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 11-10 06:34 | +10 | ETH | DOWN | 0.62 | 0.75 | 0.99 |
| 11-10 06:34 | +10 stop | NEAR | UP | 0.54 | open |  |
| 11-10 06:34 | +5 | NEAR | UP | 0.54 | 0.60 | 0.25 |
| 11-10 06:33 | +15 | BNB | DOWN | 0.62 | open |  |
| 11-10 06:33 | +10 stop | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-10 06:33 | +10 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 11-10 06:33 | +5 | HYPE | DOWN | 0.63 | open |  |
| 11-10 06:33 | +5 | ETH | DOWN | 0.55 | 0.61 | 0.25 |
| 11-10 06:33 | +10 stop | ZEC | DOWN | 0.52 | open |  |
| 11-10 06:33 | +5 | XRP | DOWN | 0.65 | 0.74 | 0.60 |
| 11-10 06:33 | +10 stop | BNB | DOWN | 0.66 | open |  |
| 11-10 06:33 | +10 | BNB | DOWN | 0.66 | open |  |
| 11-10 06:33 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-10 06:33 | +10 stop | SOL | DOWN | 0.66 | open |  |
| 11-10 06:33 | +20 | SOL | DOWN | 0.66 | open |  |
| 11-10 06:33 | +15 | SOL | DOWN | 0.66 | open |  |
| 11-10 06:33 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-10 06:33 | +5 | SOL | DOWN | 0.66 | open |  |
| 11-10 06:32 | +10 stop | DOGE | UP | 0.56 | 0.36 | -2.35 |
| 11-10 06:32 | +5 | NEAR | DOWN | 0.49 | 0.54 | 0.14 |
| 11-10 06:32 | +10 stop | HYPE | DOWN | 0.58 | open |  |
| 11-10 06:32 | +20 | HYPE | DOWN | 0.58 | open |  |
| 11-10 06:32 | +15 | HYPE | DOWN | 0.58 | open |  |
| 11-10 06:32 | +10 | HYPE | DOWN | 0.58 | open |  |
| 11-10 06:32 | +5 | HYPE | DOWN | 0.58 | 0.65 | 0.35 |
| 11-10 06:32 | +5 | BTC | DOWN | 0.47 | 0.57 | 0.64 |
| 11-10 06:32 | +10 stop | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 11-10 06:32 | +20 | XRP | DOWN | 0.51 | 0.74 | 1.98 |
| 11-10 06:32 | +15 | XRP | DOWN | 0.51 | 0.67 | 1.26 |
| 11-10 06:32 | +10 | XRP | DOWN | 0.51 | 0.64 | 0.95 |
| 11-10 06:32 | +5 | XRP | DOWN | 0.51 | 0.56 | 0.14 |
| 11-10 06:32 | +10 stop | ETH | DOWN | 0.50 | 0.61 | 0.75 |
| 11-10 06:32 | +20 | ETH | DOWN | 0.48 | 0.75 | 2.38 |
| 11-10 06:32 | +15 | ETH | DOWN | 0.48 | 0.75 | 2.38 |
| 11-10 06:32 | +10 | ETH | DOWN | 0.49 | 0.59 | 0.65 |
| 11-10 06:32 | +5 | ETH | DOWN | 0.49 | 0.56 | 0.34 |
| 11-10 06:32 | +10 stop | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-10 06:32 | +20 | BNB | DOWN | 0.50 | 0.70 | 1.67 |
