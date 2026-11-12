# Range-Scalp Bot

*Updated Thu Nov 12 12:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56909 | 49611 | 7298 (101) | 6 | $-15651.73 | -4.4% |
| **+10¢** | 42532 | 34019 | 8513 (133) | 6 | $-14569.14 | -5.4% |
| **+15¢** | 35660 | 26496 | 9164 (167) | 6 | $-13181.68 | -5.9% |
| **+20¢** | 31768 | 22153 | 9615 (217) | 6 | $-11558.40 | -5.8% |
| **+10¢ (15¢ stop)** | 69377 | 69249 | 128 (78) | 1 | $-25626.14 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 12:54 | +10 stop | XRP | UP | 0.51 | open |  |
| 11-12 12:52 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-12 12:52 | +10 | XRP | UP | 0.63 | open |  |
| 11-12 12:52 | +5 | XRP | UP | 0.64 | open |  |
| 11-12 12:48 | +10 stop | ETH | UP | 0.61 | 0.71 | 0.68 |
| 11-12 12:48 | +10 stop | ZEC | UP | 0.66 | 0.84 | 1.54 |
| 11-12 12:48 | +5 | NEAR | DOWN | 0.68 | 0.73 | 0.20 |
| 11-12 12:48 | +10 stop | DOGE | UP | 0.71 | 0.81 | 0.74 |
| 11-12 12:47 | +10 stop | NEAR | DOWN | 0.61 | 0.45 | -1.95 |
| 11-12 12:47 | +20 | NEAR | DOWN | 0.60 | 0.81 | 1.82 |
| 11-12 12:47 | +15 | NEAR | DOWN | 0.60 | 0.78 | 1.50 |
| 11-12 12:47 | +10 | NEAR | DOWN | 0.60 | 0.73 | 0.99 |
| 11-12 12:47 | +5 | NEAR | DOWN | 0.61 | 0.69 | 0.48 |
| 11-12 12:47 | +10 stop | BTC | UP | 0.62 | 0.73 | 0.79 |
| 11-12 12:47 | +10 stop | HYPE | UP | 0.66 | 0.82 | 1.33 |
| 11-12 12:47 | +20 | HYPE | UP | 0.66 | 0.89 | 2.07 |
| 11-12 12:47 | +15 | HYPE | UP | 0.66 | 0.82 | 1.33 |
| 11-12 12:47 | +10 | HYPE | UP | 0.66 | 0.82 | 1.33 |
| 11-12 12:47 | +5 | HYPE | UP | 0.66 | 0.73 | 0.40 |
| 11-12 12:47 | +5 | BNB | UP | 0.71 | 0.77 | 0.32 |
| 11-12 12:46 | +10 stop | DOGE | DOWN | 0.65 | 0.40 | -2.83 |
| 11-12 12:46 | +20 | DOGE | DOWN | 0.65 | open |  |
| 11-12 12:46 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-12 12:46 | +10 | DOGE | DOWN | 0.66 | open |  |
| 11-12 12:46 | +5 | DOGE | DOWN | 0.66 | open |  |
| 11-12 12:46 | +10 stop | SOL | DOWN | 0.54 | 0.32 | -2.54 |
| 11-12 12:46 | +20 | SOL | DOWN | 0.55 | open |  |
| 11-12 12:46 | +15 | SOL | DOWN | 0.55 | open |  |
| 11-12 12:46 | +10 | SOL | DOWN | 0.55 | open |  |
| 11-12 12:46 | +5 | SOL | DOWN | 0.56 | open |  |
| 11-12 12:46 | +10 stop | ETH | DOWN | 0.55 | 0.33 | -2.54 |
| 11-12 12:46 | +20 | ETH | DOWN | 0.55 | open |  |
| 11-12 12:46 | +15 | ETH | DOWN | 0.55 | open |  |
| 11-12 12:46 | +10 | ETH | DOWN | 0.56 | open |  |
| 11-12 12:46 | +5 | ETH | DOWN | 0.56 | open |  |
| 11-12 12:46 | +10 stop | ZEC | DOWN | 0.60 | 0.32 | -3.13 |
| 11-12 12:46 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-12 12:46 | +15 | ZEC | DOWN | 0.60 | open |  |
| 11-12 12:46 | +10 | ZEC | DOWN | 0.60 | open |  |
| 11-12 12:46 | +5 | ZEC | DOWN | 0.60 | open |  |
