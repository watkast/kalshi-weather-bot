# Range-Scalp Bot

*Updated Thu Nov 05 22:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48806 | 42535 | 6271 (74) | 8 | $-13826.92 | -4.5% |
| **+10¢** | 36425 | 29133 | 7292 (100) | 8 | $-12714.37 | -5.6% |
| **+15¢** | 30507 | 22654 | 7853 (129) | 8 | $-11597.73 | -6.1% |
| **+20¢** | 27104 | 18872 | 8232 (168) | 8 | $-10279.57 | -6.0% |
| **+10¢ (15¢ stop)** | 59481 | 59386 | 95 (57) | 3 | $-22032.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 22:37 | +10 stop | BNB | DOWN | 0.68 | open |  |
| 11-05 22:37 | +10 stop | BTC | DOWN | 0.67 | open |  |
| 11-05 22:36 | +10 stop | NEAR | UP | 0.62 | open |  |
| 11-05 22:36 | +10 stop | ETH | UP | 0.55 | 0.39 | -1.95 |
| 11-05 22:36 | +20 | ETH | UP | 0.55 | open |  |
| 11-05 22:36 | +15 | ETH | UP | 0.55 | open |  |
| 11-05 22:36 | +10 | ETH | UP | 0.55 | open |  |
| 11-05 22:36 | +5 | ETH | UP | 0.55 | open |  |
| 11-05 22:36 | +10 stop | DOGE | UP | 0.63 | 0.41 | -2.54 |
| 11-05 22:36 | +10 stop | XRP | DOWN | 0.60 | 0.70 | 0.68 |
| 11-05 22:36 | +10 stop | BNB | DOWN | 0.48 | 0.66 | 1.46 |
| 11-05 22:35 | +10 stop | NEAR | DOWN | 0.59 | 0.43 | -1.95 |
| 11-05 22:35 | +5 | NEAR | DOWN | 0.60 | open |  |
| 11-05 22:34 | +10 stop | NEAR | UP | 0.45 | 0.59 | 1.05 |
| 11-05 22:34 | +5 | NEAR | UP | 0.46 | 0.59 | 0.95 |
| 11-05 22:34 | +10 stop | DOGE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-05 22:33 | +5 | NEAR | DOWN | 0.39 | 0.55 | 1.25 |
| 11-05 22:33 | +10 stop | ZEC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-05 22:33 | +10 stop | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-05 22:33 | +20 | ETH | DOWN | 0.56 | 0.77 | 1.79 |
| 11-05 22:33 | +15 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-05 22:33 | +10 | ETH | DOWN | 0.56 | 0.74 | 1.48 |
| 11-05 22:33 | +5 | ETH | DOWN | 0.56 | 0.62 | 0.25 |
| 11-05 22:32 | +10 stop | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-05 22:32 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-05 22:32 | +10 stop | XRP | DOWN | 0.58 | 0.69 | 0.77 |
| 11-05 22:32 | +10 stop | BTC | DOWN | 0.56 | 0.40 | -1.95 |
| 11-05 22:32 | +10 stop | NEAR | DOWN | 0.59 | 0.33 | -2.93 |
| 11-05 22:32 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-05 22:32 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-05 22:32 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-05 22:32 | +5 | NEAR | DOWN | 0.59 | 0.67 | 0.47 |
| 11-05 22:31 | +10 stop | ZEC | UP | 0.58 | 0.36 | -2.55 |
| 11-05 22:31 | +20 | ZEC | UP | 0.58 | open |  |
| 11-05 22:31 | +15 | ZEC | UP | 0.58 | open |  |
| 11-05 22:31 | +10 | ZEC | UP | 0.58 | open |  |
| 11-05 22:31 | +5 | ZEC | UP | 0.58 | open |  |
| 11-05 22:31 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-05 22:31 | +20 | HYPE | DOWN | 0.65 | 0.85 | 1.75 |
| 11-05 22:31 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
