# Range-Scalp Bot

*Updated Thu Nov 12 12:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56853 | 49557 | 7296 (101) | 6 | $-15668.80 | -4.4% |
| **+10¢** | 42491 | 33980 | 8511 (133) | 6 | $-14597.56 | -5.5% |
| **+15¢** | 35625 | 26464 | 9161 (167) | 8 | $-13220.18 | -5.9% |
| **+20¢** | 31734 | 22122 | 9612 (217) | 9 | $-11608.45 | -5.8% |
| **+10¢ (15¢ stop)** | 69326 | 69198 | 128 (78) | 2 | $-25624.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 12:03 | +10 stop | SOL | UP | 0.53 | 0.36 | -2.06 |
| 11-12 12:03 | +10 stop | ETH | UP | 0.61 | 0.34 | -3.03 |
| 11-12 12:03 | +10 stop | XRP | UP | 0.52 | open |  |
| 11-12 12:03 | +10 stop | BTC | UP | 0.66 | 0.40 | -2.93 |
| 11-12 12:02 | +5 | ETH | DOWN | 0.61 | open |  |
| 11-12 12:02 | +10 stop | XRP | DOWN | 0.56 | 0.41 | -1.85 |
| 11-12 12:02 | +20 | XRP | DOWN | 0.57 | open |  |
| 11-12 12:02 | +15 | XRP | DOWN | 0.59 | open |  |
| 11-12 12:02 | +10 | XRP | DOWN | 0.57 | open |  |
| 11-12 12:02 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-12 12:02 | +10 stop | ZEC | UP | 0.62 | open |  |
| 11-12 12:02 | +20 | ZEC | UP | 0.63 | open |  |
| 11-12 12:02 | +15 | ZEC | UP | 0.62 | open |  |
| 11-12 12:02 | +10 | ZEC | UP | 0.62 | open |  |
| 11-12 12:02 | +5 | ZEC | UP | 0.62 | open |  |
| 11-12 12:01 | +10 stop | BTC | DOWN | 0.55 | 0.40 | -1.85 |
| 11-12 12:01 | +20 | BTC | DOWN | 0.57 | open |  |
| 11-12 12:01 | +15 | BTC | DOWN | 0.59 | open |  |
| 11-12 12:01 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-12 12:01 | +5 | BTC | DOWN | 0.59 | open |  |
| 11-12 12:01 | +10 stop | BNB | DOWN | 0.66 | 0.41 | -2.83 |
| 11-12 12:01 | +20 | BNB | DOWN | 0.68 | open |  |
| 11-12 12:01 | +15 | BNB | DOWN | 0.68 | open |  |
| 11-12 12:01 | +10 | BNB | DOWN | 0.68 | open |  |
| 11-12 12:01 | +5 | BNB | DOWN | 0.68 | open |  |
| 11-12 12:01 | +10 stop | SOL | DOWN | 0.63 | 0.45 | -2.15 |
| 11-12 12:01 | +20 | SOL | DOWN | 0.62 | open |  |
| 11-12 12:01 | +15 | SOL | DOWN | 0.62 | open |  |
| 11-12 12:01 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-12 12:01 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-12 12:01 | +10 stop | ETH | DOWN | 0.60 | 0.45 | -1.85 |
| 11-12 12:01 | +20 | ETH | DOWN | 0.60 | open |  |
| 11-12 12:01 | +15 | ETH | DOWN | 0.60 | open |  |
| 11-12 12:01 | +10 | ETH | DOWN | 0.60 | open |  |
| 11-12 12:01 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.27 |
| 11-12 12:01 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-12 12:01 | +20 | HYPE | DOWN | 0.64 | open |  |
| 11-12 12:01 | +15 | HYPE | DOWN | 0.64 | open |  |
| 11-12 12:01 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 11-12 12:01 | +5 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
