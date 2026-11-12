# Range-Scalp Bot

*Updated Thu Nov 12 11:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56825 | 49532 | 7293 (101) | 3 | $-15671.10 | -4.4% |
| **+10¢** | 42470 | 33963 | 8507 (133) | 4 | $-14592.60 | -5.5% |
| **+15¢** | 35608 | 26451 | 9157 (167) | 4 | $-13219.68 | -5.9% |
| **+20¢** | 31718 | 22110 | 9608 (217) | 4 | $-11609.79 | -5.8% |
| **+10¢ (15¢ stop)** | 69292 | 69164 | 128 (78) | 3 | $-25608.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 11:23 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 11-12 11:23 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-12 11:23 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-12 11:23 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-12 11:22 | +10 stop | HYPE | DOWN | 0.55 | open |  |
| 11-12 11:22 | +20 | HYPE | DOWN | 0.55 | open |  |
| 11-12 11:22 | +15 | HYPE | DOWN | 0.55 | open |  |
| 11-12 11:22 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-12 11:22 | +5 | HYPE | DOWN | 0.56 | open |  |
| 11-12 11:22 | +10 stop | NEAR | DOWN | 0.59 | open |  |
| 11-12 11:22 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-12 11:22 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-12 11:22 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-12 11:22 | +5 | NEAR | DOWN | 0.63 | 0.68 | 0.17 |
| 11-12 11:20 | +10 stop | ZEC | UP | 0.58 | 0.76 | 1.49 |
| 11-12 11:19 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 11:19 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-12 11:19 | +15 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 11-12 11:19 | +10 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 11:19 | +5 | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-12 11:18 | +10 stop | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 11-12 11:18 | +10 | ETH | DOWN | 0.69 | 0.84 | 1.25 |
| 11-12 11:18 | +5 | ETH | DOWN | 0.69 | 0.74 | 0.21 |
| 11-12 11:17 | +10 stop | ZEC | DOWN | 0.71 | 0.50 | -2.43 |
| 11-12 11:17 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-12 11:17 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-12 11:17 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-12 11:17 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-12 11:16 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 11:16 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 11-12 11:16 | +15 | XRP | DOWN | 0.67 | 0.84 | 1.44 |
| 11-12 11:16 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 11:16 | +5 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-12 11:16 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.92 |
| 11-12 11:16 | +20 | BNB | DOWN | 0.65 | 0.96 | 2.91 |
| 11-12 11:16 | +15 | BNB | DOWN | 0.65 | 0.96 | 2.91 |
| 11-12 11:16 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.92 |
| 11-12 11:16 | +5 | BNB | DOWN | 0.65 | 0.77 | 0.92 |
| 11-12 11:16 | +10 stop | ETH | DOWN | 0.65 | 0.79 | 1.12 |
| 11-12 11:16 | +20 | ETH | DOWN | 0.65 | open |  |
